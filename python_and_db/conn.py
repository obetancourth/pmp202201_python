import sqlite3
conn = None

def get_connection():
  global conn
  if conn is None:
    conn = sqlite3.connect('iotevents.db')
  return conn
