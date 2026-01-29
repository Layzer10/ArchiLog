import click
import uuid

from dataclasses import dataclass

import sqlite3
from datetime import date
@dataclass
class Item:
    id: uuid.UUID
    name: str


@click.group()
def cli():
    pass


@cli.command()
@click.option("-n", "--name", prompt="Name", help="The name of the item.")
def createCagnote(name: str):
    item = Item(uuid.uuid4(), name)
    click.echo(item)

@cli.command()
@click.option("-n", "--name", prompt="Name", help="The name of the item.")
def deleteCagnote(id: int):
    item = Item(uuid.uuid4(), int)
    click.echo(item.name)

@cli.command()
@click.option('--item',type=(str, int, click.DateTime(formats=["%Y-%m-%d"])),
required=True)
def addParticipation(item):
    name, prix, date = item

    click.echo(f"nom={name} prix={prix} date={date.date()}")

@cli.command()
@click.option("-n", "--name", prompt="Name", help="The name of the item.")
def deleteParticipation(id: int):
    item = Item(uuid.uuid4(), id)
    click.echo(item)

createCagnote()