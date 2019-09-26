from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url_base = "https://www.todapolitica.com/eleicoes-2016/rn/"

#fields = ['rank', 'player_name', 'goals_scored', 'assists', 'minutes_played', 'matches_played', 'penalties_scored',
#         'goals_left_foot', 'goals_right_foot', 'headed_goals']


# Inicializa webdriver (**Troque pelo webdriver desejado e o caminho**)
driver = webdriver.Chrome(executable_path='./chromedriver')
# Aguarda o browser
driver.implicitly_wait(30)
# Entra na URL
driver.get(url_base)

# Obtém o elemento pai de paginação
alfabeto = driver.find_element_by_css_selector('div.alfabeto')

letters = alfabeto.find_elements_by_tag_name('li')
letters_disable = alfabeto.find_elements_by_css_selector('li.disabled')

for letter in letters:
    if letter not in letters_disable:
        # driver.get(f'https://www.todapolitica.com/eleicoes-2016/rn/{letter.text.lower()}')
        # driver.implicitly_wait(50)
        print(f'executando {letter.text}')
        # letters = alfabeto.find_elements_by_tag_name('li')
        try:
            # driver.execute_script("arguments[0].click();", letters[letter])
            letter.click()
        except:
            print('erro')
            pass
        # letter.click()
        driver.implicitly_wait(20)


'''
# Obtém o número de tags <a>
num_pages = len(pagination_base.find_elements_by_xpath('.//a'))

# Captura a tabela
goals_table = driver.find_element_by_id('goal-scored')

# Cria uma lista vazia que conterá todos os dados
goals = []

for page in range(num_pages):
    pages = pagination_base.find_elements_by_xpath('.//a')
    try:
        driver.execute_script("arguments[0].click();", pages[page])
    except:
        pass
    page.click()
    driver.implicitly_wait(2)

    rows = goals_table.find_elements_by_tag_name('tr')
    # Itera sobre cada linha da tabela
    for row in rows:
            cols = row.find_elements_by_tag_name('td')
            # Itera sobre cada célula de cada linha da tabela
            if cols:
                # Cria um dicionário para conter os dados de uma linha (jogador atual)
                goal = {}
                # Para cada célula/coluna da linha, insira a chave (nome do campo) e o valor no dicionário
                for i, field in enumerate(fields):
                    val = cols[i].text
                    try:
                        goal[field] = int(val)
                    except ValueError:
                        goal[field] = val.title()
                # Adicione o dicionário de dados do jogador atual na lista `goals`
                goals.append(goal)
                print(f'{goal["rank"]} - {goal["player_name"]}')

# Mostre todos os dados de todos os jogadores
print(goals)
'''