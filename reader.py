import csv,json

with open('citys.json', encoding='utf-8') as arq:
    citys = json.load(arq)

with open('citys.csv', 'w') as arq_csv:
    fieldnames=['name', 'voters']
    writer = csv.DictWriter(arq_csv, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(citys)