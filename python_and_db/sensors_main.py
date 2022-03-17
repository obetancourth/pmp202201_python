from webbrowser import get
from sensors_dao import create_table, add_new_event, get_all_events
from sensors_ui import header, table_row
from time import sleep
# print("Creando la Tabla y la DB")
# create_table()
# print("Eso fue todo ....")

# add_new_event('ping_smtp', 'ok:true,ts:800ms')
# sleep(3)
# add_new_event('ping_smtp', 'ok:true,ts:600ms')
# sleep(3)
# add_new_event('ping_smtp', 'ok:true,ts:300ms')
# sleep(3)
# add_new_event('ping_smtp', 'ok:true,ts:500ms')
header('CRUD de EVENTS')
table_row(get_all_events())
