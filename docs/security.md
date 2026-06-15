# Security Notes

## Purpose

This document describes the security assumptions and mitigation strategy for the LLM Reliability Platform.

The project is a public demo and engineering portfolio project, but it should still follow production-minded security practices.

## Core Risks

Important risks:

- Prompt injection
- Insecure output handling
- Sensitive information disclosure
- Model denial of service
- Supply chain vulnerabilities
- Excessive agency (Over-permissioned agent behavior)
- Cost abuse
- Unsafe file uploads
- Secret leakage

## Secrets

Secret handling rules:

- Never commit `.env`.
- Never commit API keys.
- Keep `.env.example` free of real secrets.
- Use GitHub environment secrets for deployment.
- Rotate provider keys if exposure is suspected.
- Use least privilege where possible.

## Upload Safety

Uploaded documents are untrusted input.

Controls:

- File size limits
- Allowed file types
- Text extraction error handling
- Maximum document character limits
- No execution of uploaded content
- No direct trust in document instructions

## Prompt Injection

Documents may contain malicious instructions.

Mitigations:

- System prompt defines strict behavior.
- Answers must be grounded in retrieved context.
- Citations are required.
- Refusal behavior is defined when context is insufficient.
- LLM output is not treated as executable instructions.

## Rate Limits and Cost Controls

Demo traffic must be protected by:

- Per-user or per-IP rate limits
- Daily request budget
- Upload limits
- Provider timeout limits
- Fallback behavior
- Safe error responses

## Dependency Security

Use:

- Dependabot
- Secret scanning
- Pre-commit hooks
- Dependency review where available
- Regular dependency updates

## Deployment Security

The production-like deployment should include:

- SSH key authentication
- Restricted firewall rules
- HTTPS
- Reverse proxy configuration
- Protected secrets
- Backup and restore process

## Out of Scope for v1.0

The first version does not include:

- User accounts
- Social login
- Payment data
- Multi-tenant isolation
- Customer production data
- Complex RBAC
