import time
import os

clear = os.system('cls' if os.name == 'nt' else 'clear')


def countdown(num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = f'{m:02d}:{s:02d}'
        print(min_sec_format)
        time.sleep(1)
        num_of_secs -= 1
    print(f'Acabou o tempo de {inp} segundos.')


inp = int(input('Digite o tempo em segundos: '))
countdown(inp)
