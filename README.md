# Authorized Security Engagement Pack

This pack defines a small, local-only practice engagement. It does not grant authorization to test any real system. Complete and sign `authorization-and-scope.md` with the asset owner before any assessment, including tests against assets outside the local demo.

## Contents

- `lab/` — intentionally vulnerable Python demo bound to loopback, with synthetic records only.
- `authorization-and-scope.md` — written authorization and explicit exclusions.
- `asset-inventory-and-threat-model.md` — inventory, boundaries, identities, data classes, attack surfaces, STRIDE, abuse cases, ranked mitigations.
- `rules-of-engagement.md` — windows, evidence, escalation, and safe stop conditions.

## Run the lab

Use Python 3. The server listens only on `127.0.0.1:8000`; it uses only the Python standard library and makes no outbound connections.

```powershell
cd lab
python app.py
```

In a browser, visit `http://127.0.0.1:8000/`. The demo intentionally includes a reflected HTML injection issue and an insecure direct object reference. Test only this local application. Stop with Ctrl+C. Do not port-forward, expose the port, or point tools at other hosts. All records are fabricated.

## Lab limits

This is a deliberately small teaching fixture, not a production-like target or a full security test environment. The app has no login, persistence, secrets, external dependencies, or privileged operations. Its vulnerabilities are not permission to test similarly named endpoints elsewhere. Keep the lab process local and stop it when finished.
