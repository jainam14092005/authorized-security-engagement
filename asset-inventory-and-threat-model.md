# Asset Inventory and STRIDE Threat Model

## Inventory and boundaries

This inventory describes the included local exercise, not a claim about any real organization. For a real engagement, replace each row with owner-verified values and obtain separate authorization for each target.

| Asset / component | Owner | Boundary / location | Identity & privilege | Data class | Attack surface |
|---|---|---|---|---|---|
| `lab/app.py` HTTP service | Tester for local instance | One workstation; loopback `127.0.0.1:8000` | No authentication; anonymous requests | Public demo content | `/`, `/profile?id=`, `/search?q=` |
| Synthetic record map | Lab maintainer | In process memory; no persistence | No per-record authorization (intentional flaw) | Fabricated, non-sensitive | Record identifier selection and response body |
| Browser used for exercise | Tester | Same workstation | Local user session; no app identity | Browser-local state | URL/query parsing and HTML rendering |
| Test notes/evidence | Test lead | Approved local storage | Named tester and evidence custodian | Minimal synthetic proof; engagement metadata | File access, sharing, retention, deletion |

### Trust boundaries

1. **Tester/browser to local HTTP service:** untrusted request path and query values cross into the app.
2. **Application to record data:** caller-controlled record ID selects a record; the demo intentionally has no authorization check.
3. **Application response to browser renderer:** reflected query input crosses into HTML without context-appropriate encoding.
4. **Evidence to engagement owner:** notes or screenshots leave tester control only via the approved channel and custodian.

No external identity provider, network service, database, cloud account, or real data store is part of the lab.

## Data classes and identities

- **Data:** public instructions; fabricated profile fields; operational engagement metadata; evidence consisting only of minimal proof and synthetic values. No credentials, secrets, real personal information, or production data are needed.
- **Identities:** anonymous application caller; local workstation user running the process; authorized tester; test lead; asset owner/approver; evidence custodian. The demo does not authenticate or distinguish application users.
- **Authorization expectation:** in a real application, a verified identity should be bound to an explicit resource permission check for every record request. The exercise demonstrates the absence of that check; it does not simulate real account access.

## STRIDE analysis and abuse cases

| STRIDE | Abuse case / affected boundary | Impact | Likelihood in a real analogue | Ranked mitigation |
|---|---|---|---|---|
| Spoofing | Anonymous caller is treated as an authorized user because the demo has no authentication boundary. | Unauthorized access in a real service. | High if exposed and data is sensitive. | **P1:** authenticate callers; use centralized identity and session controls; require MFA for privileged paths. Not needed to add real identities to this toy lab. |
| Tampering | Caller changes `id` to select another synthetic record; no resource-level authorization is evaluated. | Cross-account data exposure or unauthorized update in a real analogue. | High where identifiers are guessable and checks are absent. | **P1:** enforce server-side object authorization on every read/write; scope queries to the authenticated principal; deny by default; audit denials. |
| Repudiation | Minimal service log does not establish which authenticated actor made a request or what decision was made. | Weak accountability and incident reconstruction. | Medium. | **P2:** produce protected audit events with actor, resource, action, decision, timestamp, and correlation ID; minimize sensitive data in logs. |
| Information disclosure | `/profile` returns record fields for a caller-selected ID; `/search` reflects unescaped input into HTML. | Synthetic data disclosure in lab; sensitive data exposure or script execution in an analogous real app. | High when deployed without controls. | **P1:** object-level authorization and context-aware output encoding; add restrictive CSP as defense in depth; avoid sensitive data in responses. |
| Denial of service | Repeated or oversized requests can consume the simple single-threaded server's capacity. | Local demo becomes unavailable; analogous service degradation. | Low for the isolated demo; environment-dependent in production. | **P2:** do not load-test this fixture; production rate limits, request-size/time limits, concurrency controls, and monitoring. |
| Elevation of privilege | An unauthenticated caller can reach any record because the app has no roles or per-object checks. | Higher-privilege or cross-tenant access in a real analogue. | High if authorization is omitted. | **P1:** least privilege, server-side role and tenant checks, secure defaults, and negative authorization tests. |

### Ranked mitigation plan

1. **P1 — Access control:** require authentication where applicable, then authorize every resource and action server-side; bind lookup to the caller's tenant/principal; return the same safe denial for unauthorized and nonexistent objects where appropriate.
2. **P1 — Output handling:** encode untrusted data for its exact HTML context or render it as text; avoid unsafe HTML construction; deploy a restrictive Content Security Policy as a secondary control.
3. **P1 — Exposure control:** keep the exercise loopback-only, use synthetic records, and prohibit forwarding/tunneling. In production, expose only through approved ingress and TLS.
4. **P2 — Accountability and resilience:** log authorization decisions without secrets, apply request limits and monitoring, and define an incident path.
5. **P2 — Verification:** after fixes, repeat only the approved minimal checks and retain evidence of both allowed and denied behavior.

## Exercise abuse cases and expected safe outcomes

- Request another **synthetic** record ID in the lab to observe missing object authorization. Do not substitute real identifiers or targets. Stop if any non-synthetic information appears.
- Submit a harmless HTML marker in the lab search parameter to observe reflection. Do not use payloads that access browser storage, make network calls, or affect other users. Stop if browser behavior escapes the local demo.
- Confirm the service is reachable only on loopback by local inspection. Do not scan the workstation or surrounding network.
