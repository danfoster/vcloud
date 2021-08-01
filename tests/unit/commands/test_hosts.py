from click.testing import CliRunner
import pytest


from vcloud.cli import main

class TestHosts:

    def test_list(self, config_file):
        """
        Checks that we can list defined hosts
        """
        runner = CliRunner()

        result = runner.invoke(main, ["hosts", "list"])
        assert result.exit_code == 0, result.output
        assert result.output == """name    uri
------  ---------------
test1   test:///default
"""


    def test_add(self, config_file):
        runner = CliRunner()
        hostname = "test"
        hosturi = "test:///test2"
        result = runner.invoke(main, ["hosts", "add", hostname, hosturi])
        assert result.exit_code == 0

    @pytest.mark.parametrize("hostname,expected_return_code,expected_stdout", [
        ("test1", 0, ""),
        ("test_does_not_exist", 2, (
            "Usage: main hosts set [OPTIONS] NAME\n"
            "Try 'main hosts set --help' for help.\n"
            "\n"
            "Error: Unknown Host test_does_not_exist\n"
        )),
    ])
    def test_set(self, hostname, expected_return_code, expected_stdout, config_file):
        runner = CliRunner()
        result = runner.invoke(main, ["hosts", "set", hostname])
        assert result.exit_code == expected_return_code, result.output
        assert result.output == expected_stdout
