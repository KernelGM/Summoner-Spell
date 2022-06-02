import time
import ttkbootstrap as ttk
from ttkbootstrap.constants import BOTH, YES, LEFT, RIGHT


def countdown(num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = f'{m:02d}:{s:02d}'
        print(min_sec_format)
        time.sleep(1)
        num_of_secs -= 1
    print(f'Acabou o tempo de {num_of_secs} segundos.')


# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
root = ttk.Window(title='Summoner Spell',
                  iconphoto=None,
                  themename='superhero',
                  alpha=1,
                  minsize=(255, 105))

root.geometry('270x130+1085+50')
root.attributes('-topmost', True)
root.overrideredirect(1)

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
summoner_spells = sorted([
    'Barrier', 'Cleanse', 'Exhaust', 'Flash',
    'Ghost',  'Heal', 'Ignite', 'Smite', 'Teleport'])

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
notebook_tab = ttk.Notebook(master=root)
notebook_tab.pack(side=LEFT, padx=10, pady=10, expand=YES, fill=BOTH)


def lanes(set_lane):
    main_frame = ttk.Frame(master=root)
    main_frame.pack(fill=BOTH, expand=YES, padx=5, pady=5)

    frame_d = ttk.Frame(master=main_frame)
    frame_d.pack(fill=BOTH, expand=YES)

    label_d = ttk.Label(master=frame_d, text='Marque o Spell')
    label_d.pack(side=LEFT, padx=5, pady=5)

    button_d = ttk.Button(master=frame_d, text='START')
    button_d.pack(side=RIGHT, padx=5, pady=5)

    combobox_d = ttk.Combobox(
        master=frame_d, values=summoner_spells, state='readonly')
    combobox_d.pack(side=RIGHT, padx=5, pady=5)
    combobox_d.current(3)

    frame_f = ttk.Frame(master=main_frame)
    frame_f.pack(fill=BOTH, expand=YES)

    label_f = ttk.Label(master=frame_f, text='Marque o Spell')
    label_f.pack(side=LEFT, padx=5, pady=5)

    button_f = ttk.Button(master=frame_f, text='START')
    button_f.pack(side=RIGHT, padx=5, pady=5)

    combobox_f = ttk.Combobox(
        master=frame_f, values=summoner_spells, state='readonly')
    combobox_f.pack(side=RIGHT, padx=5, pady=5)
    combobox_f.current(8)

    notebook_tab.add(main_frame, text=set_lane)


lanes('TOP')
lanes('JNG')
lanes('MID')
lanes('ADC')
lanes('SUP')

root.mainloop()
