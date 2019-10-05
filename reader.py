import csv,json

with open('dados/citys_by_letter_results.json', encoding='utf-8') as arq:
    citys_by_letter_results = json.load(arq)

with open('dados/citys_results.csv', 'w') as arq_csv:
    fieldnames=['name','voters', 'votos_brancos', 'votos_nulos', 'vagas_vereadores', 'url']
    writer = csv.DictWriter(arq_csv, fieldnames=fieldnames)
    writer.writeheader()

    for citys_by_letter in citys_by_letter_results.values():
        for x, y in citys_by_letter['citys'].items():
            writer.writerow({'name': x, 'voters': y['voters'], 'votos_brancos': y['votos_brancos'], 'votos_nulos': y['votos_nulos'], 'vagas_vereadores': y['vagas_vereadores'], 'url': y['url']})
