# Rules of Engagement

## Operating controls

- **Preconditions:** signed authorization is on file; scope, owner, tester list, dates, timezone, contacts, and evidence custodian are completed; testers have reviewed the exclusions and stop rules.
- **Target verification:** before each session, confirm the browser address is exactly `http://127.0.0.1:8000/` and the tester started their own copy of `lab/app.py`. Do not follow links away from that origin.
- **Test window:** only during the owner-approved interval entered in the authorization record. The local exercise has no separate availability window; the owner should still record the session time. No testing after expiry or revocation.
- **Rate and method:** manual, low-rate requests only. No scanners, fuzzers, automated crawling, concurrency, stress testing, destructive requests, persistence, or external callbacks.
- **Change control:** do not change service binding, firewall rules, DNS, host files, routes, or lab code to widen reach. Stop before any activity that could alter data or affect another service.

## Evidence handling

- Capture the least evidence needed to show the issue, using only synthetic records and the local origin. Prefer a short note with timestamp, URL path, observed behavior, and sanitized screenshot.
- Never collect or retain passwords, tokens, cookies, personal data, or unrelated system information. If encountered unexpectedly, stop, do not copy or explore it, and notify the owner through the escalation path.
- Store evidence in the approved restricted location, encrypt it at rest where supported, and limit access to the named test lead, owner, and custodian. Do not place evidence in public issue trackers or unapproved cloud storage.
- Transfer only through the owner-approved channel. Record who handled evidence and when. Retain until the agreed date: ____________________. Then securely delete working copies and confirm deletion to the custodian.
- Report findings with asset, time, minimal reproduction, impact, evidence reference, and mitigation. Keep raw evidence separate from the report.

## Escalation

| Severity / event | Required response | Notify |
|---|---|---|
| Any unexpected real data, credential, secret, or non-synthetic record | Stop immediately; do not inspect further; preserve only the fact of occurrence, not the data; follow owner instructions for secure handling. | Owner and test lead via approved emergency channel |
| Target/address differs from the approved local origin, or scope is ambiguous | Stop requests and close the session until the owner confirms written scope. | Test lead, then owner |
| Service instability, unexpected side effects, or possible impact to another system | Stop immediately; preserve concise timestamps and symptoms; do not attempt recovery actions unless the owner directs them. | Owner and test lead |
| Suspected compromise or active incident | Stop testing; do not investigate beyond preserving minimal context; hand off to the owner's incident response contact. | Owner's incident lead and test lead |
| Routine finding within scope | Complete minimal proof, record it, and report through the agreed channel. | Test lead and owner |

## Immediate stop conditions

Stop all testing immediately if any of the following occurs:

1. Written authorization is absent, expired, unclear, narrowed, or revoked.
2. The destination is not exactly the local loopback lab, or any request would cross the workstation boundary.
3. Real personal, customer, regulated, confidential, credential, or non-synthetic data appears.
4. A test may modify/delete data, degrade availability, trigger an external side effect, or affect a third party.
5. The app binds beyond loopback, is exposed by forwarding/tunneling, or is reachable by another device.
6. The owner, test lead, or incident responder directs a halt.

After stopping: cease requests, close the lab process if safe, do not broaden investigation, record time and reason without copying sensitive content, and notify the named contacts. Resume only after the owner provides explicit written direction and any required scope correction.

## Session closeout

At the end of each window, stop the process, confirm no test activity remains, account for evidence, report any stop event, and send the owner a concise status. Do not leave the demo running unattended.
