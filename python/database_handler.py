import sqlite3
from js import console
conn = sqlite3.connect('test.db')

def create():
    console.log("Creating database...")