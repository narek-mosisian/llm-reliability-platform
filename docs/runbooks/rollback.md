# Runbook: Rollback

## Purpose

This runbook describes how to roll back a failed deployment.

## Access Requirements

This runbook is intended for maintainers or operators with production deployment access.

External contributors can help by identifying the regression, linking the failing commit, attaching logs or opening a fix pull request. They are not expected to perform production rollback steps.

## Symptoms

Rollback may be needed when:

- API health check fails
- Web app is unreachable
- Database migration breaks the app
- Error rate increases after deployment
- Eval quality regresses after release
- Critical security issue is introduced

## Immediate Checks

1. Identify the deployed commit.
2. Check container status.
3. Check the API health endpoint.
4. Check recent logs.
5. Check Grafana error panels.
6. Identify whether a database migration is involved.

## Rollback Strategy

Preferred rollback:

```text
Deploy the previous known-good commit or image.
```

## Manual Rollback Steps

1. SSH into the server.
2. Navigate to the deployment directory.
3. Check the current commit.
4. Checkout the previous known-good commit.
5. Rebuild or pull containers.
6. Restart services with Docker Compose.
7. Run smoke tests.

Example:

```bash
git log --oneline -5
git checkout <previous-good-commit>
docker compose -f docker-compose.prod.yml up -d --build
```

## Database Considerations

If a migration was applied:

- Check whether a rollback migration exists.
- Avoid destructive rollback without backup.
- Restore from backup only if necessary and understood.

## Validation

After rollback:

- API health endpoint works.
- Web app loads.
- Demo request works.
- Error rate stabilizes.
- Grafana shows recovery.

## Evidence

Store:

- Failed deployment commit
- Rolled back commit
- Reason for rollback
- Smoke test result
- Dashboard screenshot

Use:

```text
evidence/ci-reports/
evidence/screenshots/
```
