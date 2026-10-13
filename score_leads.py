"""Rank inbound signup accounts from a HubSpot contact export.

Usage:
    python score_leads.py [input_csv] [output_csv]

Defaults to inbound_signups.csv -> ranked_accounts.csv.
"""

import sys

import pandas as pd

# HubSpot's default export headers. Change these if your export uses different ones.
EMAIL_COL = "Email"
DATE_COL = "Create Date"
COMPANY_COL = "Company Name"
FIRST_NAME_COL = "First Name"
LAST_NAME_COL = "Last Name"

# Matched on the first label of the domain, so gmail.com, yahoo.co.uk,
# outlook.fr and icloud.com are all dropped.
PERSONAL_PROVIDERS = {"gmail", "yahoo", "outlook", "icloud"}

MULTI_THREADED_MIN = 2


def score(input_path, output_path):
    df = pd.read_csv(input_path)

    missing = [c for c in (EMAIL_COL, DATE_COL) if c not in df.columns]
    if missing:
        sys.exit(
            f"Missing column(s) {missing} in {input_path}. "
            f"Found: {list(df.columns)}. Update the column names at the top of this script."
        )

    df[EMAIL_COL] = df[EMAIL_COL].astype("string").str.strip().str.lower()
    df = df[df[EMAIL_COL].str.contains("@", na=False)].copy()
    df["company_domain"] = df[EMAIL_COL].str.split("@").str[-1]

    provider = df["company_domain"].str.split(".").str[0]
    df = df[~provider.isin(PERSONAL_PROVIDERS)].copy()

    df[DATE_COL] = pd.to_datetime(df[DATE_COL], errors="coerce", format="mixed")

    if FIRST_NAME_COL in df.columns and LAST_NAME_COL in df.columns:
        names = (
            df[FIRST_NAME_COL].fillna("").astype(str)
            + " "
            + df[LAST_NAME_COL].fillna("").astype(str)
        ).str.strip()
        df["contact"] = names.where(names != "", df[EMAIL_COL])
    else:
        df["contact"] = df[EMAIL_COL]

    agg = {
        "signup_count": (EMAIL_COL, "nunique"),
        "most_recent_signup": (DATE_COL, "max"),
        "contacts": ("contact", lambda s: "; ".join(sorted(set(s)))),
        "emails": (EMAIL_COL, lambda s: "; ".join(sorted(set(s)))),
    }
    if COMPANY_COL in df.columns:
        agg["company_name"] = (
            COMPANY_COL,
            lambda s: s.dropna().mode().iat[0] if s.notna().any() else "",
        )

    accounts = df.groupby("company_domain", as_index=False).agg(**agg)
    accounts["multi_threaded"] = accounts["signup_count"] >= MULTI_THREADED_MIN

    accounts = accounts.sort_values(
        ["multi_threaded", "most_recent_signup"],
        ascending=[False, False],
        na_position="last",
    )

    first = ["company_domain", "company_name"] if COMPANY_COL in df.columns else ["company_domain"]
    cols = first + ["multi_threaded", "signup_count", "most_recent_signup", "contacts", "emails"]
    accounts[cols].to_csv(output_path, index=False)

    multi = int(accounts["multi_threaded"].sum())
    print(f"Wrote {len(accounts)} accounts to {output_path} ({multi} multi-threaded).")


if __name__ == "__main__":
    in_path = sys.argv[1] if len(sys.argv) > 1 else "inbound_signups.csv"
    out_path = sys.argv[2] if len(sys.argv) > 2 else "ranked_accounts.csv"
    score(in_path, out_path)
