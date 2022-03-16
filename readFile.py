archivo = open("data/meeting_saved_chat.txt", "r", encoding='utf-8')
cuentas = list()
modificadores = list()
nombre=''
for line in archivo:
  if line.find("From") >= 0:
    start = line.find("From") + 5
    end = line.find("to") - 1
    nombre = line[start: end]
  else:
    cuenta = line.strip()
    nueva_cuenta = dict()
    nueva_cuenta['Nombre'] = nombre
    nueva_cuenta['Cuenta'] = cuenta
    cuentas.append(nueva_cuenta)

opcion = ''
while opcion != 'S':
  print("=" * 40)
  print("Remplazo de Cuentas")
  print("Cuentas Registradas: " + len(cuentas) )
  print("Modificadores Registrados: " + len(modificadores))
  print("=" * 40)
  print ("Agregar Modificadores: M ")
  print ("Reemplazar Valores: R ")
  print ("Salir del Programa: S")
  opcion = input("Escribar un opcion y presione Enter:").strip().upper()
  if opcion == 'M':
    opcionModificadores = ''
    while opcionModificadores != 'N':
      print("=" * 40)
      print ("Agregar Modificadores")
      
  elif opcion == 'R':
    
