import libvirt
import re

STATES = [
    "",
    "RUNNING",
    "BLOCKED",
    "PAUSED",
    "SHUTDOWN",
    "SHUTOFF",
    "CRASHED",
    "SUSPENDED",
]



class Instance:

    def __init__(self, domain):
        self.domain = domain


    @property
    def mem(self):
        return self.domain.maxMemory()

    @property
    def name(self):
        return self.domain.name()

    @property
    def state(self):
        state, reason = self.domain.state()
        return STATES[state]

    @property
    def cpus(self):
        return self.domain.vcpusFlags()


    def start(self):
        """
        Starts an instance
        """
        print(f"Starting {self.name}...")
        try:
            self.domain.create()
        except libvirt.libvirtError as error:
            print(error)

    def stop(self):
        """
        Stops and instance
        """
        print(f"Stopping {self.name}...")
        try:
            self.domain.shutdown()
        except libvirt.libvirtError as error:
            print(error)

    def dump(self):
        return {
            "Name": self.name,
            "State": self.state,
            "Memory": self.mem,
            "CPUS": self.cpus,
        }
        