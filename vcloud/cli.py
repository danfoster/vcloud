import click
import logging

from .commands import instances

logger = logging.getLogger(__name__)

@click.group()
def main():
    pass

main.add_command(instances.instances)