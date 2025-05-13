import pytest
from click.testing import CliRunner
from genix.cli import main


def test_cli_set_up_new_repo():
    runner = CliRunner()
    result = runner.invoke(main, ["set up new repo"])
    assert result.exit_code == 0
    assert "Genix suggests: git init" in result.output
