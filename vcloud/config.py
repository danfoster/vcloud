import yaml
import os
import pathlib
import logging
import sys

from .host import Host

logger = logging.getLogger(__name__)


class Config:

    filename = os.path.expanduser("~/.config/vcloud/vcloud.conf")

    def __init__(self):
        self.load(self.filename)
        self.set_defaults()

    def __del__(self):
        self.save(self.filename)

    def load(self, filename):
        """
        Loads the configration from disk
        """

        if not os.path.exists(filename):
            dirname = os.path.dirname(filename)
            pathlib.Path(dirname).mkdir(parents=True, exist_ok=True)
            pathlib.Path(filename).touch()
            self.config = {}

        with open(filename) as file:
            self.config = yaml.load(file, Loader=yaml.FullLoader) or {}

    def save(self, filename):
        """
        Saves the configuration to disk
        """
        if not os.path.exists(filename):
            dirname = os.path.dirname(filename)
            pathlib.Path(dirname).mkdir(parents=True, exist_ok=True)

        with open(filename, 'w') as file:
            yaml.dump(self.config, file)

    def get(self, key):
        return self.config[key]

    def set(self, key, value):
        self.config[key] = value

    def get_hosts(self):
        """
        Gets a list of defined hosts
        """
        hosts = []
        for h in self.get("hosts"):
            hosts.append(Host(h['name'], h['uri']))
        return hosts

    def add_host(self, name, uri):
        """
        Adds a new host to the config
        """
        hosts = self.get("hosts")
        existing_names = [x["name"] for x in hosts]
        if name in existing_names:
            logger.error("%s already exists", name)
            sys.exit(1)

        self.config['hosts'].append({
            "name": name,
            "uri": uri
        })

    def get_active_host(self):
        hosts = self.get_hosts()
        activehostname = self.get("active_host")
        for host in hosts:
            if host.name == activehostname:
                return host

    def set_defaults(self):
        try:
            self.get("hosts")
        except KeyError:
            logger.warning("No hosts defined")
            self.set("hosts", [])

    def validate(self):
        """
        Checks the current config is valid and sets any sensible defaults
        """
        try:
            active_host = self.get("active_host")
        except KeyError:
            logger.error("No active host set, set with: vcloud hosts set")
            sys.exit(1)

        host_names = [x["name"] for x in self.get("hosts")]
        if active_host not in host_names:
            logger.error(
                f"No host named \"{active_host}\" found in the configuration"
            )
            sys.exit(1)
