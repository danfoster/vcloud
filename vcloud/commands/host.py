import click
import logging

from ..host import get_hosts
from .. import outputters

logger = logging.getLogger(__name__)

@click.group()
def host():
    pass

@host.command()
@click.pass_context
def list(ctx):
    """
    """
    config = ctx[]
    hosts = get_hosts()
    instances = host.get_instances()
    outputters.table([ x.dump() for x in instances])