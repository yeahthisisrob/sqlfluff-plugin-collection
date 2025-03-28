from setuptools import setup, find_packages

setup(
    name="sqlfluff_plugins",
    version="0.1.0",
    description=(
        "A SQLFluff plugin collection extending SQL linting capabilities with custom rules " "and templater plugins."
    ),
    packages=find_packages(),
    entry_points={
        "sqlfluff": [
            "plugins = sqlfluff_plugins",
        ]
    },
)
