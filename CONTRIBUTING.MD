## Pre-commit Hooks

We use [pre-commit](https://pre-commit.com/) to enforce code style and linting before commits.

### Setup
```bash
# Install pre-commit
pip install pre-commit

# Install hooks
pre-commit install

# Run hooks manually (optional)
pre-commit run --all-files
