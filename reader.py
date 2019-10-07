from os import listdir
import csv, json

if __name__ == '__main__':
    # Converte os dados de todos os estados 
    print('Working: ', end='')
    for file in sorted(listdir('./data/')):
        print('#', end='')
        
        with open(f'./data/{file}', encoding='utf-8') as arq:
            cities_by_letter_results = json.load(arq)

        with open(f"./csv_data/electionData_{file.split('_')[1].split('.')[0]}.csv", 'w') as arq_csv:
            fieldnames = [
                'uf', 'name', 'voters', 
                'votos_brancos', 'votos_nulos', 
                'vagas_vereadores'
            ]

            writer = csv.DictWriter(arq_csv, fieldnames=fieldnames)
            writer.writeheader()

            for city in cities_by_letter_results.values():
                for name, data in city['citys'].items():
                    writer.writerow({
                        'uf': file.split('_')[1].split('.')[0],
                        'name': name, 
                        'voters': data['voters'], 
                        'votos_brancos': data['votos_brancos'], 
                        'votos_nulos': data['votos_nulos'], 
                        'vagas_vereadores': data['vagas_vereadores']
                    })

    print('\nDone!')