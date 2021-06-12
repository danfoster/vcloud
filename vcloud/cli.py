import click
import logging

from .commands import instances
from .commands import hosts
from .config import Config

logger = logging.getLogger(__name__)

@click.group()
@click.pass_context
def main(ctx):
    ctx.ensure_object(dict)
    ctx.obj['config'] = Config()

main.add_command(instances.instances)
main.add_command(hosts.hosts)