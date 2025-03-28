# sqlfluff-plugin-collection

A collection of custom SQLFluff plugins to extend SQL linting with additional rules.  
Currently includes a rule enforcing vertical formatting for `CASE` expressions.

---

## Features

- ✅ Vertical formatting rule (`VF01`)
    - Ensures `THEN` appears on a new line after `WHEN` in `CASE` expressions.
    - Helps enforce consistent, readable SQL formatting.
  
## Requirements

- Python 3.8+
- SQLFluff >=2.1.0

---

## Installation

Clone and install the plugin in editable mode:

```bash
git clone https://github.com/your-username/sqlfluff-plugin-collection.git
cd sqlfluff-plugin-collection
pip install -e .
```

Verify that SQLFluff detects the plugin:

```bash
sqlfluff rules
```

You should see your custom rule (`VF01`) listed.

---

## Usage

Simply run SQLFluff like usual:

```bash
sqlfluff lint path/to/your/file.sql
sqlfluff fix path/to/your/file.sql
```

Your custom rules will automatically be applied.

---

## Example

Bad (inline formatting):

```sql
CASE WHEN condition THEN result ELSE fallback END
```

Good (vertical formatting):

```sql
CASE
    WHEN condition
        THEN result
    ELSE fallback
END
```

---

### Example SQL file

You can find an example SQL file under [`examples/case_statements_example.sql`](./examples/case_statements_example.sql):

```bash
sqlfluff lint examples/case_statements_example.sql
sqlfluff fix examples/case_statements_example.sql
```

This file contains both a violating (inline) and a compliant (vertical) CASE expression to test the rule.

---

## Development

### Pre-commit hooks (optional)

Install and configure pre-commit to automatically run Black and Flake8:

```bash
pre-commit install
pre-commit run --all-files
```

---

## License

MIT License

---

## References

- [SQLFluff Plugin Documentation](https://docs.sqlfluff.com/en/stable/guides/contributing/plugins.html)
- [SQL Style Guide (Recommended)](https://www.sqlstyle.guide/)
