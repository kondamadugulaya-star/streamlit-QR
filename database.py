import sqlite3

def get_connection():
    return sqlite3.connect("attendance.db", check_same_thread=False)
