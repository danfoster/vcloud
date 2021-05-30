import libvirt
import logging

from .instance import Instance

logger = logging.getLogger(__name__)

class Host:

    def __init__(self, uri):
        self.uri = uri
        self.conn = libvirt.open(self.uri)

    def get_instances(self):
        domains = self.conn.listAllDomains()
        if domains == None:
            logger.error("Failed to get a list of VMs")
            return []
        
    
        instances = [] 
        for domain in domains:
            instances.append(Instance(domain))

        return instances
        
