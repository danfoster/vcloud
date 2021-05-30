import click
import logging

from ..host import Host
from .. import outputters

logger = logging.getLogger(__name__)

@click.group()
def instances():
    pass

@instances.command()
@click.pass_context
def list(ctx):
    """
    """
    host = Host("qemu+ssh://zem@10.42.2.100/system")
    instances = host.get_instances()
    outputters.table([ x.dump() for x in instances])