# Security Policy

## Supported Versions

This project is currently in early development. Security fixes are applied to the latest version on the `main` branch.

| Version | Supported |
|---|---|
| main | Yes |
| older branches | No |

## Reporting a Vulnerability

Please do not open public issues for suspected security vulnerabilities.

Report security concerns by creating a private security advisory on GitHub if available, or by contacting the project maintainer through the repository profile.

Include:

- A short description of the issue
- Steps to reproduce
- Affected files, endpoints, or configuration
- Potential impact
- Suggested mitigation, if known

## Security Scope

Security work for this project includes:

- Secret handling
- Environment variable hygiene
- Prompt injection risks
- Insecure output handling
- Upload safety
- Rate limits
- Cost abuse prevention
- Provider fallback safety
- Dependency updates
- CI security checks
- Deployment hardening

## Out of Scope

The following are out of scope for the first version:

- Public multi-tenant authentication
- Payment processing
- Customer production data
- Custom model training security
- Kubernetes cluster security

## Principles

- No secrets are committed to the repository.
- `.env` files are ignored.
- `.env.example` documents configuration without real secrets.
- Demo uploads must be treated as untrusted input.
- LLM outputs must not be treated as trusted executable instructions.
- Provider keys must be protected with least privilege and rotation procedures.
