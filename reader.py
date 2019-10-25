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
                'uf', 'municipio', 'eleitores', 
                'votosBrancos', 'votosNulos', 
                'vagasVeriador'
            ]

            writer = csv.DictWriter(arq_csv, fieldnames=fieldnames)
            writer.writeheader()

            for city in cities_by_letter_results.values():
                for name, data in city['citys'].items():
                    writer.writerow({
                        'uf': file.split('_')[1].split('.')[0],
                        'municipio': name, 
                        'eleitores': data['voters'], 
                        'votosBrancos': data['votos_brancos'], 
                        'votosNulos': data['votos_nulos'], 
                        'vagasVeriador': data['vagas_vereadores']
                    })

    print('\nDone!')