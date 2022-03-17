def header(title):
  print("="* 60)
  titleLen = len(title)
  middle = int((60 - titleLen) / 2)
  print((" "*middle) + title)
  print("="* 60)

def table_row(rows):
  for item in rows:
    id = item[0]
    timestamp = item[1]
    origin = item[2]
    status = item[3]
    print(id, timestamp, origin, status, sep="\t")
