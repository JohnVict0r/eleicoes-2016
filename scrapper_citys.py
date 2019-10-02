from selenium import webdriver
import json

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

letters= []
citys = dict()

# Pegando apenas as letras habilitadas
for letter in letters_element:
    if letter not in letters_disable_element:
        letters.append(letter.text.lower())

# Pegar as cidades para cada letra habilitada da lista do alfabeto do estado
for letter in letters:
    # Navegar para a lista de cidades da letra habilitada
    driver.get(f'{url_base}{letter}')
    driver.implicitly_wait(5)

    # pegando a lista de cidades
    city_list_by_letter = driver.find_element_by_css_selector('div.lista-estados')
    city_list = city_list_by_letter.find_elements_by_tag_name('li')

    for city in city_list:
        try:
            url = city.find_element_by_tag_name('a').get_attribute('href')
            voters = int(city.find_element_by_tag_name('span').text.strip(' eleitores').replace('.', ''))
            citys[city.find_element_by_tag_name('a').text] = {'voters': voters , 'url': url}

        except Exception as e:
            print(e)
            pass

# Salvando no arquivo
with open('dados/pre_citys.json', 'w') as arq:
    json.dump(citys, arq)
