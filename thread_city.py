from selenium import webdriver

def get_city_results(data):
    print('Executando thread...', data['url'])

    # Inicializa webdriver (**Troque pelo webdriver desejado e o caminho**)
    driver = webdriver.Chrome(executable_path='./chromedriver')
    # Aguarda o browser
    driver.implicitly_wait(10)

    try:
        # Entra na URL
        driver.get(data['url'])

        print('aguarde...')
        resultados = driver.find_elements_by_css_selector('div.results-foo')
        custom = driver.find_element_by_css_selector('ul.custom')

        # TODO pegar resultados para prefeitos e para vereadores
        # resultados_prefeito = resultados[0].find_elements_by_tag_name('span')
        # resultados_vereadores = resultados[1].find_elements_by_tag_name('span')

        votos_brancos = resultados[1].find_elements_by_tag_name('span')[1].text.split(':')[1]
        votos_nulos = resultados[1].find_elements_by_tag_name('span')[2].text.split(':')[1]
        vagas_vereadores = custom.find_element_by_tag_name('li').text.split(':')[1]

        data['votos_brancos'] = int(votos_brancos.replace(',', ''))
        data['votos_nulos'] = int(votos_nulos.replace(',', ''))
        data['vagas_vereadores'] = int(vagas_vereadores.replace(',', ''))

    except Exception as e:
        print(e)
        driver.close()

    driver.close()
    print('Terminou!')


def get_citys_by_letter(data):
    print('Executando thread...', data['url'])

    # Inicializa webdriver (**Troque pelo webdriver desejado e o caminho**)
    driver = webdriver.Chrome(executable_path='./chromedriver')
    # Aguarda o browser
    driver.implicitly_wait(10)

    try:
        # Navegar para a lista de cidades da letra habilitada
        driver.get(data['url'])
        # pegando a lista de cidades
        city_list_by_letter = driver.find_element_by_css_selector('div.lista-estados')
        city_list = city_list_by_letter.find_elements_by_tag_name('li')

        for city in city_list:
            url = city.find_element_by_tag_name('a').get_attribute('href')
            voters = int(city.find_element_by_tag_name('span').text.strip(' eleitores').replace('.', ''))
            name = city.find_element_by_tag_name('a').text
            data['citys'].update({name: {'voters': voters, 'url': url}})

    except Exception as e:
        print(e)
        driver.close()

    driver.close()
    print('Terminou!')