import csv,json

with open('citys.json', encoding='utf-8') as arq:
    citys = json.load(arq)


with open('citys.csv', 'w') as arq_csv:
    fieldnames=['name','voters', 'url', 'votos_brancos', 'votos_nulos', 'vagas_vereadores']
    writer = csv.DictWriter(arq_csv, fieldnames=fieldnames)
    writer.writeheader()

    for x,y in citys.items():
        print(x,y)
        row = dict()
        row['name'] = x

        writer.writerow()
    #writer.writerows(citys)