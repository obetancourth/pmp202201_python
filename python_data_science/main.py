import csv
from unittest import skip
# python -m pip install csv
# pip install csv

import matplotlib.pyplot as plt
# python -m pip install matplotlib
# pip intall matplotlib

with open('data/Machine_readable_file_bdc_sf_2021_q4.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  dic_grouping = dict()
  axs_value = list()
  lbls_value = list()
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
    axs_value.append(dic_grouping[data]["value"]/1000)
    lbls_value.append(dic_grouping[data]["series"][0:10])
    # print(dic_grouping[data])

plt.bar(range(0,len(axs_value)), axs_value)
plt.xticks(range(0,len(axs_value)), lbls_value, rotation=45)
plt.ylabel('Series')
plt.title('Series de Ingresos')
plt.show()
