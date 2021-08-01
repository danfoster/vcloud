import pytest

from vcloud.config import Config


@pytest.fixture(scope="session")
def monkeysession(request):
    """
    Session scoped version of monkeypatch, taken from:
    https://github.com/pytest-dev/pytest/issues/363
    """
    from _pytest.monkeypatch import MonkeyPatch
    mpatch = MonkeyPatch()
    yield mpatch


@pytest.fixture(scope="session", autouse=True)
def config_file(request, tmp_path_factory, monkeysession):
    filename = tmp_path_factory.mktemp("config") / "config.yml"
    filename.write_text("""
active_host: test1
hosts:
- name: test1
  uri: test:///default
    """)
    monkeysession.setattr(Config, "filename", filename)
