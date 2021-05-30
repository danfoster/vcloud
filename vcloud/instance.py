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

    def dump(self):
        return {
            "Name": self.name,
            "State": self.state,
            "Memory": self.mem,
            "CPUS": self.cpus,
        }
        