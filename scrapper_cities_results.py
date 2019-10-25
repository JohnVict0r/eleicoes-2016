import json
from os import listdir
import concurrent.futures
from thread_city import get_city_results

if __name__ == '__main__':

    for file in listdir('./preData'):
        print(f"Tratando os dados de {file.split('_')[2].split('.')[0]}...")

        # Abrir a lista de cidades
        with open(f'preData/{file}', encoding='utf-8') as arq:
            cities_by_letter = json.load(arq)

        cities = {}
        for c in cities_by_letter.values():
            cities.update(c['cities'])

        print(cities)
        # Distribuir em threads o processo de capturar os resultados de cada cidade
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            executor.map(get_city_results, cities.values())

        for a in cities_by_letter.values():
            for old_city in a.values():
                for new_city in cities.keys():
                    if new_city == old_city:
                        old_city[new_city] = cities[new_city]

        # Salvando no arquivo
        with open(f"data/electionData_{file.split('_')[2].split('.')[0]}.json", 'w') as arq:
            json.dump(cities_by_letter, arq)
