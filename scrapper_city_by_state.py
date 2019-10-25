from selenium import webdriver
import json
import concurrent.futures
from thread_city import get_cities_by_letter

if __name__ == '__main__':
    states = [
        {'uf': 'AC', 'url': 'https://www.todapolitica.com/eleicoes-2016/ac/'},
        {'uf': 'AL', 'url': 'https://www.todapolitica.com/eleicoes-2016/al/'},
        {'uf': 'AM', 'url': 'https://www.todapolitica.com/eleicoes-2016/am/'},
        {'uf': 'AP', 'url': 'https://www.todapolitica.com/eleicoes-2016/ap/'},
        {'uf': 'BA', 'url': 'https://www.todapolitica.com/eleicoes-2016/ba/'},
        {'uf': 'CE', 'url': 'https://www.todapolitica.com/eleicoes-2016/ce/'},
        {'uf': 'ES', 'url': 'https://www.todapolitica.com/eleicoes-2016/es/'},
        {'uf': 'GO', 'url': 'https://www.todapolitica.com/eleicoes-2016/go/'},
        {'uf': 'MA', 'url': 'https://www.todapolitica.com/eleicoes-2016/ma/'},
        {'uf': 'MG', 'url': 'https://www.todapolitica.com/eleicoes-2016/mg/'},
        {'uf': 'MS', 'url': 'https://www.todapolitica.com/eleicoes-2016/ms/'},
        {'uf': 'MT', 'url': 'https://www.todapolitica.com/eleicoes-2016/mt/'},
        {'uf': 'PA', 'url': 'https://www.todapolitica.com/eleicoes-2016/pa/'},
        {'uf': 'PB', 'url': 'https://www.todapolitica.com/eleicoes-2016/pb/'},
        {'uf': 'PE', 'url': 'https://www.todapolitica.com/eleicoes-2016/pe/'},
        {'uf': 'PI', 'url': 'https://www.todapolitica.com/eleicoes-2016/pi/'},
        {'uf': 'PR', 'url': 'https://www.todapolitica.com/eleicoes-2016/pr/'},
        {'uf': 'RJ', 'url': 'https://www.todapolitica.com/eleicoes-2016/rj/'},
        {'uf': 'RN', 'url': 'https://www.todapolitica.com/eleicoes-2016/rn/'},
        {'uf': 'RO', 'url': 'https://www.todapolitica.com/eleicoes-2016/ro/'},
        {'uf': 'RR', 'url': 'https://www.todapolitica.com/eleicoes-2016/rr/'},
        {'uf': 'RS', 'url': 'https://www.todapolitica.com/eleicoes-2016/rs/'},
        {'uf': 'SC', 'url': 'https://www.todapolitica.com/eleicoes-2016/sc/'},
        {'uf': 'SE', 'url': 'https://www.todapolitica.com/eleicoes-2016/se/'},
        {'uf': 'SP', 'url': 'https://www.todapolitica.com/eleicoes-2016/sp/'},
        {'uf': 'TO', 'url': 'https://www.todapolitica.com/eleicoes-2016/to/'}        
    ]

    for state in states:
        print(f'Recolhendo os dadaos de {state["uf"]}')

        url_base = state['url']

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

        cities_by_letter_links = dict()

        # Pegando apenas as letras habilitadas
        for letter in letters_element:
            if letter not in letters_disable_element:
                cities_by_letter_links[letter.text.upper()] = {
                    'url': f'{url_base}{letter.text.lower()}', 
                    'cities': {}
                }

        # Distribuir em threads o processo de capturar os resultados de cada cidade
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            executor.map(get_cities_by_letter, cities_by_letter_links.values())

        # Salvando no arquivo
        with open(f'preData/pre_cities_{state["uf"]}.json', 'w') as arq:
            json.dump(cities_by_letter_links, arq)
