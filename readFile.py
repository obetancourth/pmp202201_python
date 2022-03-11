archivo = open("data/meeting_saved_chat.txt", "r",)
for line in archivo:
  if line.find("From") >= 0:
    start = line.find("From") + 5
    end = line.find("to") - 1
    nombre = line[start: end]
    print(nombre, end="\t")
  else:
    cuenta = line.strip()
    print(cuenta)
