# Objective: Learn how to define and run a function in python.
def diga_hola():
  print("\n"*5 + "Hola" + "\n")

def print_list(list_to_print):
  print('Elementos en la Lista: ' , len(list_to_print))
  for list_item in list_to_print:
    print(list_item)

# Profundizar el uso de comprensión | lambda en python
def print_only_r(list_to_print):
  filtered_list = [item for item in list_to_print if 'r' in item]
  print_list(filtered_list)

diga_hola()
lst_nombres_colores = ['rojo', '255', '#fff', 'rosado']
lst_nombres_colores.append('white')

print_list(lst_nombres_colores)
print_only_r(lst_nombres_colores)

# Dictionaries
dic_clientes = {
  'nombre' : 'Fulanito de Tal',
  'edad' : 25,
  'correo': 'uncorreo@provider.com'
}

lst_clientes = list()
lst_clientes.append(dic_clientes)
lst_clientes.append({
  'nombre' : 'Menganito de Tal',
  'edad' : 15,
  'correo': 'uncorreo2@provider.com'
})
print(lst_clientes)

for cliente in lst_clientes:
  print(cliente['nombre'])
