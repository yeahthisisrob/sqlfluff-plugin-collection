# Contributing to sqlfluff-plugin-collection

Thank you for considering contributing! This project welcomes contributions of all kinds, including new rules, improvements to existing rules, bug fixes, and documentation updates.

## How to Contribute

### 1. Fork and Clone
Fork this repository and clone it locally:
```bash
git clone https://github.com/your-username/sqlfluff-plugin-collection.git
cd sqlfluff-plugin-collection
```

### 2. Create a Virtual Environment
It's recommended to use a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

### 3. Install Dependencies
Install the plugin and development tools:
```bash
pip install -e .
pip install -r requirements-dev.txt  # if available
```

### 4. Format and Lint
Make sure code passes formatting and linting:
```bash
black .
flake8
```

### 5. Pre-commit (optional but recommended)
Install pre-commit hooks:
```bash
pre-commit install
pre-commit run --all-files
```

### 6. Testing
If you add rules or logic, please provide an example SQL file under `/examples/` to demonstrate or test it.

### 7. Commit Guidelines
- Use clear and meaningful commit messages.
- Follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) style if possible.

### 8. Pull Requests
- Open a pull request to `main`.
- Describe what your contribution changes.
- If applicable, mention related issues.
- Be open to feedback.

---

## Code Style

- Formatting is enforced using **Black** (`black .`)
- Linting is done via **Flake8** (`flake8`)
- Recommended max line length is `88`

---

Thank you for contributing to the project!
