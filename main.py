from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import concurrent.futures
import threading
from thread_city import my_thread

url_base = "https://www.todapolitica.com/eleicoes-2016/rn/"

# Inicializa webdriver (**Troque pelo webdriver desejado e o caminho**)
driver = webdriver.Chrome(executable_path='chromedriver')
# Aguarda o browser
driver.implicitly_wait(30)
# Entra na URL
driver.get(url_base)

# Obtém o elemento pai de paginação
alfabeto = driver.find_element_by_css_selector('div.alfabeto')

letters_element = alfabeto.find_elements_by_tag_name('li')
letters_disable_element = alfabeto.find_elements_by_css_selector('li.disabled')

letters= []

citys = dict()

# Pegando as letras habilitadas
for letter in letters_element:
    if letter not in letters_disable_element:
        letters.append(letter.text.lower())

for letter in letters:
    driver.get(f'{url_base}{letter}')
    driver.implicitly_wait(10)

    state_list = driver.find_elements_by_css_selector('div.lista-estados')
    
    for state in state_list:
        city_elements = state.find_elements_by_tag_name('li')

        for element in city_elements:
            url = element.find_element_by_tag_name('a').get_attribute('href')
            citys[element.find_element_by_tag_name('a').text] = {'voters': element.find_element_by_tag_name('span').text, 'url': url}


with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    executor.map(my_thread, citys.values())


print(citys)


# Salvando no arquivo
with open('citys.json', 'w') as arq:
    json.dump(citys, arq)
    #TODO adicionar utf-8

# print(citys)      