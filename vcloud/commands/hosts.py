import click
import logging

from .. import outputters

logger = logging.getLogger(__name__)


@click.group()
def hosts():
    pass


@hosts.command()
@click.pass_context
def list(ctx):
    """
    Lists all defined hosts
    """
    config = ctx.obj['config']
    hosts = config.get_hosts()
    outputters.table([x.dump() for x in hosts])


@hosts.command()
@click.pass_context
@click.argument('name')
@click.argument('uri')
def add(ctx, name, uri):
    """
    Adds a host to the config
    """
    config = ctx.obj['config']
    config.add_host(name, uri)


@hosts.command()
@click.pass_context
@click.argument('name')
def set(ctx, name):
    """
    Sets the active host
    """
    config = ctx.obj['config']
    host_names = [x["name"] for x in config.get("hosts")]
    if name not in host_names:
        raise click.BadArgumentUsage("Unknown Host {}".format(name))
    config.set("active_host", name)
    logger.info("Set active host to: %s", name)
