# bdr-toolkit

Template library for outbound and inbound touches. Swap in `{first_name}`, `{company}` and `{detail}` before sending. The last-attempt voicemail also uses `{phone}`. `{detail}` reads best as a verb phrase that finishes "you...", like "posted about moving off Snowflake."

House rules for every template: warm, human, curious-first. Lowercase is fine. No bullet points, no em dashes, no exclamation points, under 80 words, and never a list of three.

## inbound-replies

| Template | When to use it |
| --- | --- |
| [new-signup.md](inbound-replies/new-signup.md) | Someone creates a MotherDuck account and you want to learn why before pitching anything. |
| [content-download.md](inbound-replies/content-download.md) | Someone downloads a guide or registers for content and you want to find the problem behind it. |

## linkedin

| Template | When to use it |
| --- | --- |
| [missed-email.md](linkedin/missed-email.md) | Your email bounced or went unanswered and you're reopening the thread on LinkedIn. Best performer. |
| [connection-note.md](linkedin/connection-note.md) | Cold connection request where you want to signal curiosity, not a pitch. Fits the 300 character limit. |

## follow-ups

| Template | When to use it |
| --- | --- |
| [no-reply-bump.md](follow-ups/no-reply-bump.md) | First email got silence and you're bumping it a few days later. |
| [after-call.md](follow-ups/after-call.md) | Same-day note after a discovery call that keeps the thread warm without asking for anything. |

## voicemails

| Template | When to use it |
| --- | --- |
| [first-touch.md](voicemails/first-touch.md) | First cold call that hits voicemail. Pair it with an email the same day. |
| [last-attempt.md](voicemails/last-attempt.md) | Final call in a sequence, when you're stepping back without burning the bridge. |

## sequences

| Template | When to use it |
| --- | --- |
| [cold-prospect.md](sequences/cold-prospect.md) | Seven-day cold sequence built on one idea, labeling text in SQL. Pulls in the voicemail and LinkedIn templates on days 3 and 5. |

## trials

For people already in a trial. These also use `{ae_name}`. Lines in [brackets] are yours to fill in by hand. Each template ends with where it came from and how it did.

| Template | When to use it |
| --- | --- |
| [usage-opener.md](trials/usage-opener.md) | Trial user is moving fast. `{detail}` is what they did, like "loaded data with dlt and built Dives on top within two days." |
| [extension-reply.md](trials/extension-reply.md) | They ask for more trial time. Extend, but tie it to what the PoC has to prove. |
| [stack-playback.md](trials/stack-playback.md) | They've told you their stack and asked something. `{detail}` is their stack. |
| [feature-nudge.md](trials/feature-nudge.md) | Steady querying, no conversation yet. `{detail}` is the one feature that fits their usage. |
| [pricing-question.md](trials/pricing-question.md) | They ask a pricing question. Answer it, ask what they're building, no call. |
| [what-didnt-work.md](trials/what-didnt-work.md) | Read before sending any of the above. |
