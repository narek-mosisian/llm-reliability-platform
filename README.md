## License and Attribution

Code is licensed under the Apache License 2.0.

Documentation, diagrams, screenshots and written project materials are licensed
under CC BY 4.0.

If this project is used, forked, modified, referenced or extended, please retain
the NOTICE file and provide attribution to the original project where reasonably possible.

## Code Quality Hooks

This project uses `pre-commit` to run local quality checks before commits.

Install the Git hooks once after cloning the repository:

```bash
pre-commit install
```

Run all configured hooks manually:

```bash
pre-commit run --all-files
```

`pre-commit install` registers the local Git hooks in `.git/hooks/`. This step is required for every local clone because Git hooks are not automatically installed when the repository is cloned.

`pre-commit run --all-files` is useful after the initial setup or before opening a pull request to verify the whole repository.
