# Web scrapping - Resultados das Eleições

## Sobre o projeto

* `scrapper_citys.py` captura o link e informações sobre as cidades por letra do estado do RN.
* `scrapper_citys_results.py` captura os resultados das cidades, através dos links capturados, distruibuindo o processo em multiplas threads.
* `thread_city.py` é uma thread responsável por capturar o resultado de um cidade.
* `reader.py` fazer a leitura dos dados/arquivos gerados pelos scripts e gera um arquivo .csv melhor para permitir trabalhos futuros.
* `dados` apresenta os arquivos resultantes do web scrapping

## Configurações

`$ pip install -r requirements.txt`

obs.: é necessário ter um driver instalado, por exemplo o 'chromedriver', para ser utilizado pelo `selenium`

## Executar

`$ python scrapper_citys.py`

`$ python scrapper_citys_results.py`

`$ python reader.py`

