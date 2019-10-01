import time


def my_thread(data):
    print('Executando thread...', data['url'])
    time.sleep(2)
    data['algonovo'] = 4
    print('Terminou...')