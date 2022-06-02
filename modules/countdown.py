import time


def countdown(num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = f'{m:02d}:{s:02d}'
        print(min_sec_format)
        time.sleep(1)
        num_of_secs -= 1
    print(f'Acabou o tempo de {num_of_secs} segundos.')
