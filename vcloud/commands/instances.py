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
    config = ctx.obj['config']
    config.validate()
    host = config.get_active_host()
    instances = host.get_instances()
    logger.info("Instances on: %s", host.name)
    outputters.table([ x.dump() for x in instances])