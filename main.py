from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url_base = "https://www.todapolitica.com/eleicoes-2016/rn/"

# Inicializa webdriver (**Troque pelo webdriver desejado e o caminho**)
driver = webdriver.Chrome(executable_path='./chromedriver')
# Aguarda o browser
driver.implicitly_wait(30)
# Entra na URL
driver.get(url_base)

# Obtém o elemento pai de paginação
alfabeto = driver.find_element_by_css_selector('div.alfabeto')

letters_element = alfabeto.find_elements_by_tag_name('li')
letters_disable_element = alfabeto.find_elements_by_css_selector('li.disabled')

letters= []

citys = []

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
            
            info = element.text.split('\n')
            citys.append({'name': info[0], 'voters': info[1]})
            
            #print(f'cidade: {city.find_elements_by_tag_name('span')}')
            #print(f'eleitores: {city.find_element_by_tag_name('span').text}')
print(citys)      