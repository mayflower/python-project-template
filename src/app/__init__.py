"""Starter package. Rename it in pyproject.toml and src/ when you begin."""


def greet(name: str) -> str:
    """Return a greeting for ``name``."""
    return f"Hello, {name}!"


def main() -> None:
    """Entry point for the ``app`` command."""
    print(greet("world"))
