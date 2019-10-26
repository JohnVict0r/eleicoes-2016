import json
import concurrent.futures
from thread_city import get_city_results

# Abrir a lista de cidades
with open('dados/pre_citys.json', encoding='utf-8') as arq:
    citys_by_letter = json.load(arq)

citys = {}
for c in citys_by_letter.values():
    citys.update(c['citys'])

print(citys)
# Distribuir em threads o processo de capturar os resultados de cada cidade
with concurrent.futures.ThreadPoolExecutor(max_workers=9) as executor:
    executor.map(get_city_results, citys.values())

for a in citys_by_letter.values():
    for old_city in a.values():
        for new_city in citys.keys():
            if new_city == old_city:
                old_city[new_city] = citys[new_city]

# Salvando no arquivo
with open('dados/citys_by_letter_results.json', 'w') as arq:
    json.dump(citys_by_letter, arq)
