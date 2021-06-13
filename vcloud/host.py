import libvirt
import logging

from .instance import Instance

logger = logging.getLogger(__name__)



class Host:

    def __init__(self, name, uri):
        self.name = name
        self.uri = uri
        self.conn = libvirt.open(self.uri)

    def _build_instance_dict(self):
        """
        Builds a dict of instances in k/v of "name": "Instance"
        """
        domains = self.conn.listAllDomains()
        if domains == None:
            logger.error("Failed to get a list of VMs")
            return []
        
    
        instances = {}
        for domain in domains:
            instance = Instance(domain)
            instances[instance.name] = instance
        
        return instances


    def get_instances(self):
        """
        Returns a list of all instances
        """
        return self._build_instance_dict().values()

    def get_instance(self, name):
        """
        Returns a single instance matching the name
        """
        instances = self._build_instance_dict()
        try:
            return instances[name]
        except KeyError:
            logger.error("No instance named %s found", name)
            return None

    def dump(self):
        return {
            "name": self.name,
            "uri": self.uri,
        }
        
