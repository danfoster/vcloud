
from vcloud.config import Config


class TestConfig:

    def test_no_config_file(self, monkeypatch, tmp_path):
        """
        Checks creating a config file if none exists.
        """
        filename = tmp_path / "new_config.yml"
        
        monkeypatch.setattr(Config, "filename", filename)
        config = Config()
        assert config.filename == filename
        monkeypatch.undo()
