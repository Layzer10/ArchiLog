import click
import uuid

from dataclasses import dataclass

import sqlite3
from datetime import date

from adodbapi.examples.db_print import db

db = sqlite3.connect("cagnotte.db")


def init_db():
    db.execute("CREATE TABLE Cagnotte(idC INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT)")
    db.execute("CREATE TABLE Participant(name TEXT)")
    db.execute("CREATE TABLE Participation(idP INTEGER PRIMARY KEY AUTOINCREMENT, idC INTEGER FOREIGN KEY references Cagnotte(idC),UNIQUE (name TEXT FOREIGN KEY references Participant(name)))")
    db.execute("CREATE TABLE Depenses(idC INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT FOREIGN KEY references Participant(name),date DATE,montant REAL)")
    db.execute("INSERT INTO Participant(name) VALUES ('<Esteban>')")
    db.execute("INSERT INTO Participant(name) VALUES ('<Test>')")

@dataclass
class Item:
    id: uuid.UUID
    name: str


@click.group()
def cli():
    pass


@cli.command()
@click.option("-n", "--name", prompt="Name", help="The name of the item.")
def createCagnotte(name: str):
    item = Item(uuid.uuid4(), name)
    click.echo(item)
    db.execute("INSERT INTO Cagnotte(name) VALUES (?)", (name,))

@cli.command()
@click.option("-n", "--name", prompt="Name", help="The name of the item.")
def deleteCagnotte(name: str):
    click.echo(f"cagnotte {name} supprimée")
    db.execute("DELETE FROM Cagnotte WHERE name=?", (name,))

@cli.command()
@click.option('--item',type=(int, int),
required=True)
def addParticipation(item):
    id, name = item

    click.echo(f"nom du participant={name} id={id} date={date.date()}")

@cli.command()
@click.option("-n", "--name", prompt="Name", help="The name of the item.")
def deleteParticipation(id: int):
    item = Item(uuid.uuid4(), id)
    click.echo(item)

@cli.command()
@click.option('--item',type=(str, int, click.DateTime(formats=["%Y-%m-%d"])),
required=True)
def addDepenses(item):
    name, prix, date = item
    db.execute("INSERT INTO Depenses(name,montant,date) VALUES (?,?,?)", (name,prix,date))
    click.echo(f"nom={name} prix={prix} date={date}")