from click.testing import CliRunner


from vcloud.cli import main


class TestConfig:

    def test_list(self):
        runner = CliRunner()
     
        result = runner.invoke(main, ["hosts", "list"])
        assert result.exit_code == 0
        assert result.output == """name    uri
------  ---------------
test1   test:///default
"""