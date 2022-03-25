import csv
from unittest import skip
# python -m pip install csv
# pip install csv

with open('data/Machine_readable_file_bdc_sf_2021_q4.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  dic_grouping = dict()
  is_first_line = True
  for csv_line in csv_reader:
    if is_first_line:
      is_first_line = False
      continue
    valorstr = csv_line[2]
    if valorstr == '':
      valorstr='0'
    valor = float(valorstr)
    series = csv_line[10]
    if series in dic_grouping:
      dic_grouping[series]['value'] += valor
      dic_grouping[series]['count'] += 1
    else:
      dic_grouping[series] = {"series": series, "value": valor, "count": 1}
  for data in dic_grouping:
    print(dic_grouping[data])
