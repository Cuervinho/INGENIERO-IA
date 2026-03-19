# db/connection.py

import sqlite3

DB_PATH = "assessment_ia.db"

def get_connection():
    return sqlite3.connect(DB_PATH)