from click.testing import CliRunner

from paftdunk.cli import main


def test_hello_world():
    runner = CliRunner()
    result = runner.invoke(main, ["hello", "vincent"])
    assert "hello" in result.output
    assert "vincent" in result.output
