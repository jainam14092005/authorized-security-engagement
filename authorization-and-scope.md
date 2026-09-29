# Written Authorization and Scope

> **Authorization is not effective until completed and signed by an authorized asset owner.** This template is not itself evidence of permission. The local demo is the only target authorized by this pack absent a separately executed scope.

## Engagement record

| Field | Value |
|---|---|
| Engagement name / ID | ______________________________ |
| Asset owner / authorizing organization | ______________________________ |
| Test lead and organization | ______________________________ |
| Authorized testers | ______________________________ |
| Start and end (date, time zone) | ______________________________ |
| Approved test windows | ______________________________ |
| Emergency contact and escalation channel | ______________________________ |
| Evidence custodian | ______________________________ |

## Authorized target

For the included exercise only: the tester's own local instance of `lab/app.py`, launched on the same workstation and reachable only at `http://127.0.0.1:8000/`. The process is expected to bind to loopback. Only the synthetic records shipped in the lab are in scope.

Any additional host, domain, IP address, cloud tenant, account, application, vendor, shared service, or production/staging environment requires a separate written scope signed by its owner. Authorization for one asset does not extend to connected systems or other tenants.

## Authorized purpose and permitted activity

Purpose: practice asset-aware web application assessment and validate controls against the two documented demo weaknesses (record-level authorization and output encoding). Permitted activity is manual, low-rate browsing and requests to the local demo, collection of minimal proof using synthetic data, and reporting findings to the listed owner. No destructive testing, persistence, or access beyond the demo is authorized.

## Explicitly out of scope

- Any non-loopback destination, other user's machine, public or private network, or service reached through the workstation.
- Real, production, staging, third-party, cloud, or shared assets, even if linked from or technically reachable by the lab.
- Phishing, social engineering, credential collection, password guessing, credential stuffing, malware, persistence, or privilege escalation.
- Denial of service, load/stress testing, destructive changes, data modification/deletion, or testing that impacts availability.
- Accessing real personal, regulated, confidential, or customer information.
- Port forwarding, tunneling, proxying, remote exposure, or changing the lab bind address to a non-loopback interface.

## Approval

I have authority to approve the target and window above, have reviewed the exclusions and stopping rules, and authorize only the stated activity.

**Asset owner / approver:** ______________________________  **Title:** ____________________

**Signature:** __________________________________________  **Date/time/time zone:** ____________________

**Test lead acceptance:** ________________________________  **Date/time/time zone:** ____________________

**Change or withdrawal of authorization:** The owner may narrow, suspend, or revoke this authorization at any time through the escalation channel above. Testers stop immediately upon notice.
