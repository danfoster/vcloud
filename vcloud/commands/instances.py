"""
CLI sub-commands under the "instances" command
"""
import click
import logging

from .. import outputters

logger = logging.getLogger(__name__)


@click.group()
def instances():
    pass


@instances.command()
@click.pass_context
def list(ctx):
    """
    Lists all instances against the current active host
    """
    config = ctx.obj['config']
    config.validate()
    host = config.get_active_host()
    instances = host.get_instances()
    logger.info("Instances on: %s", host.name)
    outputters.table([x.dump() for x in instances])


@instances.command()
@click.pass_context
@click.argument('instance_name')
def start(ctx, instance_name):
    """
    Starts an instance
    """
    config = ctx.obj['config']
    config.validate()
    host = config.get_active_host()
    instance = host.get_instance(instance_name)
    if instance is None:
        # No instance found by that name
        raise click.BadArgumentUsage(
            "Unknown instance {}".format(instance_name)
        )
    instance.start()


@instances.command()
@click.pass_context
@click.argument('instance_name')
def stop(ctx, instance_name):
    """
    Stops an instance
    """
    config = ctx.obj['config']
    config.validate()
    host = config.get_active_host()
    instance = host.get_instance(instance_name)
    if instance is None:
        # No instance found by that name
        raise click.BadArgumentUsage(
            "Unknown instance {}".format(instance_name)
        )
    instance.stop()
