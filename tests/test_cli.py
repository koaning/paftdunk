from click.testing import CliRunner

from paftdunk.cli import cli


def test_hello_world():
    runner = CliRunner()
    result = runner.invoke(cli, ['hello', 'vincent'])
    assert "hello" in result.output
    assert "vincent" in result.output

