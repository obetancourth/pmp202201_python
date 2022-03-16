from sensors_dao import create_table, add_new_event
from time import sleep
# print("Creando la Tabla y la DB")
# create_table()
# print("Eso fue todo ....")

add_new_event('ping_smtp', 'ok:true,ts:800ms')
sleep(3)
add_new_event('ping_smtp', 'ok:true,ts:600ms')
sleep(3)
add_new_event('ping_smtp', 'ok:true,ts:300ms')
sleep(3)
add_new_event('ping_smtp', 'ok:true,ts:500ms')
