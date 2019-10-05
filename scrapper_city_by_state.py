from selenium import webdriver
import json
import concurrent.futures
from thread_city import get_citys_by_letter

# TODO capturar de todos os estados
url_base = "https://www.todapolitica.com/eleicoes-2016/rn/"

# Inicializa webdriver (**Troque pelo webdriver desejado e o caminho**)
driver = webdriver.Chrome(executable_path='./chromedriver')
# Aguarda o browser
driver.implicitly_wait(30)
# Entra na URL
driver.get(url_base)

# Obtém a lista do alfabeto
alfabeto = driver.find_element_by_css_selector('div.alfabeto')

# Obtém os elementos que representam as letras
letters_element = alfabeto.find_elements_by_tag_name('li')

# Obtém os elementos que representam as letras desabilitadas
letters_disable_element = alfabeto.find_elements_by_css_selector('li.disabled')

citys_by_letter_links = dict()

# Pegando apenas as letras habilitadas
for letter in letters_element:
    if letter not in letters_disable_element:
        citys_by_letter_links[letter.text.upper()] = {'url': f'{url_base}{letter.text.lower()}', 'citys': {}}

# Distribuir em threads o processo de capturar os resultados de cada cidade
with concurrent.futures.ThreadPoolExecutor(max_workers=9) as executor:
    executor.map(get_citys_by_letter, citys_by_letter_links.values())

print(citys_by_letter_links)
# Salvando no arquivo
with open('dados/pre_citys.json', 'w') as arq:
    json.dump(citys_by_letter_links, arq)
