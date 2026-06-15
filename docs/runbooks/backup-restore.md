# Runbook: Backup and Restore

## Purpose

This runbook describes the planned backup and restore process for PostgreSQL data.

## Scope

Backups should cover:

- PostgreSQL database
- Uploaded document metadata
- Chunks
- Embeddings
- Eval results
- Audit data

Uploaded raw files may require separate volume backups if stored outside the database.

## Backup Command

Planned backup script:

```text
scripts/backup-postgres.sh
```

Expected behavior:

- Create timestamped PostgreSQL dump
- Store backup in a safe location
- Avoid committing backup files
- Log backup result

## Restore Command

Planned restore script:

```text
scripts/restore-postgres.sh
```

Expected behavior:

- Stop dependent services if needed
- Restore selected backup
- Run validation checks
- Restart services
- Run smoke tests

## Backup Frequency

Initial recommendation:

```text
Manual backups before deployment changes.
Daily backups after public demo deployment.
```

## Restore Validation

After restore:

1. Check database connection.
2. Check document table count.
3. Check chunk table count.
4. Run API health check.
5. Run demo query.
6. Run a small eval subset.

## Safety Notes

- Do not overwrite production data without a verified backup.
- Do not store backups in Git.
- Do not store secrets inside backup filenames.
- Test restore before relying on backups.

## Evidence

Store restore test summaries in:

```text
evidence/ci-reports/
evidence/load-tests/
```
