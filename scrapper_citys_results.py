import json
import concurrent.futures
from thread_city import get_city_results

# Abrir a lista de cidades
with open('dados/pre_citys.json', encoding='utf-8') as arq:
    citys = json.load(arq)

# Distribuir em threads o processo de capturar os resultados de cada cidade
with concurrent.futures.ThreadPoolExecutor(max_workers=9) as executor:
    executor.map(get_city_results, citys.values())

# Salvando no arquivo
with open('dados/citys_results.json', 'w') as arq:
    json.dump(citys, arq)