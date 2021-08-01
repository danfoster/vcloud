from click.testing import CliRunner
import pytest

from vcloud.cli import main


class TestInstances:

    def test_list(self, config_file):
        """
        Checks that we can list instances
        """
        runner = CliRunner()

        result = runner.invoke(main, ["instances", "list"])
        assert result.exit_code == 0
        assert result.output == (
            "Name    State      Memory    CPUS\n"
            "------  -------  --------  ------\n"
            "test    RUNNING   8388608       2\n"
        )

    @pytest.mark.parametrize("vmname,expected_return_code,expected_stdout", [
        ("test", 0, (
            "Starting test...\n"
            "internal error: Domain 'test' is already running\n"
        )),
        ("test_does_not_exist", 2, (
            "Usage: main instances start [OPTIONS] INSTANCE_NAME\n"
            "Try 'main instances start --help' for help.\n"
            "\n"
            "Error: Unknown instance test_does_not_exist\n"
        )),
    ])
    def test_start(self, vmname, expected_return_code, expected_stdout, config_file):
        """
        Checks that we can start an instance
        """
        runner = CliRunner()
        result = runner.invoke(main, ["instances", "start", vmname])
        assert result.exit_code == expected_return_code
        assert result.output == expected_stdout

    @pytest.mark.parametrize("vmname,expected_return_code,expected_stdout", [
        ("test", 0, (
            "Stopping test...\n"
        )),
        ("test_does_not_exist", 2, (
            "Usage: main instances stop [OPTIONS] INSTANCE_NAME\n"
            "Try 'main instances stop --help' for help.\n"
            "\n"
            "Error: Unknown instance test_does_not_exist\n"
        )),
    ])
    def test_stop(self, vmname, expected_return_code, expected_stdout, config_file):
        """
        Checks that we can start an instance
        """
        runner = CliRunner()
        result = runner.invoke(main, ["instances", "stop", vmname])
        assert result.exit_code == expected_return_code
        assert result.output == expected_stdout
