# bdr-toolkit

## score_leads.py

Turns a HubSpot export of inbound signups into a ranked list of accounts.

It drops personal emails (gmail, yahoo, outlook, icloud, any country variant
like `yahoo.co.uk`), groups people by email domain, counts how many people from
each company signed up, and flags any company with 2+ signups as
`multi_threaded`. Multi-threaded accounts go first, then everything is sorted
by most recent signup.

### Run it

Needs Python 3 and pandas (`pip install pandas` if you don't have it).

1. Export contacts from HubSpot to CSV and save it in this folder as
   `inbound_signups.csv`.
2. Run:

   ```
   python score_leads.py
   ```

3. Open `ranked_accounts.csv`.

Different file names work too: `python score_leads.py my_export.csv my_output.csv`

### Columns it expects

HubSpot's default headers: `Email` and `Create Date` (required), plus
`First Name`, `Last Name`, `Company Name` (optional). If your export names them
differently, edit the constants at the top of `score_leads.py`.

### Output

| column | meaning |
| --- | --- |
| company_domain | email domain, e.g. `acme.io` |
| company_name | most common HubSpot company name for that domain |
| multi_threaded | True if 2+ people signed up |
| signup_count | unique emails from that domain |
| most_recent_signup | latest `Create Date` |
| contacts / emails | who signed up |
