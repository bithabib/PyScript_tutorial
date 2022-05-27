import sqlite3
from js import console
conn = sqlite3.connect('test.db')

def create(*args, **kwargs):
    conn.execute('''CREATE TABLE items
    (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    ietm_name           TEXT    NOT NULL,
    quantity            INT     NOT NULL)''')
    console.log("Creating database...")

def insert(*args, **kwargs):
    conn.execute("INSERT INTO items (ietm_name, quantity) VALUES ('item1', 10)")
    console.log("Inserting data...")

def fetch(*args, **kwargs):
    cursor = conn.execute("SELECT id, ietm_name, quantity from items")
    for row in cursor:
        console.log(row[0], row[1], row[2])
