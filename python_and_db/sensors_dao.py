from conn import get_connection
from datetime import datetime
def create_table():
  sql_create_statement = "CREATE TABLE IF NOT EXISTS EVENTOSIO(id INTEGER PRIMARY KEY AUTOINCREMENT, dateEvent INTEGER, origin TEXT, processed TEXT, dateProcessed INTEGER, payload TEXT );"
  conn = get_connection()
  cursor = conn.cursor()
  cursor.execute(sql_create_statement)
  conn.commit()

def add_new_event(origin_device, payload):
  sql_insert_statement = "INSERT INTO EVENTOSIO (dateEvent, origin, processed, dateProcessed, payload) values (?, ?, 'PND', 0, ?);"
  conn = get_connection()
  cursor = conn.cursor()
  timestamp = int(round(datetime.now().timestamp()))
  cursor.execute(sql_insert_statement, (timestamp, origin_device, payload))
  conn.commit()

def get_all_events():
  sql_select_statement = "SELECT * from EVENTOSIO;"
  conn = get_connection()
  cursor = conn.cursor()
  cursor.execute(sql_select_statement)
  return cursor.fetchall()
