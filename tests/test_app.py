import pytest

from app import greet, main


def test_greet() -> None:
    assert greet("Coder") == "Hello, Coder!"


def test_main_prints_greeting(capsys: pytest.CaptureFixture[str]) -> None:
    main()
    assert capsys.readouterr().out == "Hello, world!\n"
