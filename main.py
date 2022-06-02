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

root.geometry('255x105+1085+50')
root.attributes('-topmost', True)

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
summoner_spells = sorted([
    'Barrier', 'Cleanse', 'Exhaust', 'Flash',
    'Ghost',  'Heal', 'Ignite', 'Smite', 'Teleport'])

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
notebook_tab = ttk.Notebook(master=root)
notebook_tab.pack(side=LEFT, padx=10, pady=10, expand=YES, fill=BOTH)

top_label_frame = ttk.Frame(master=root)
top_label_frame.pack(fill=BOTH, expand=YES, padx=5, pady=5)

top_frame_d = ttk.Frame(master=top_label_frame)
top_frame_d.pack(fill=BOTH, expand=YES)

top_label_d = ttk.Label(master=top_frame_d, text='Marque o Spell')
top_label_d.pack(side=LEFT, padx=5, pady=5)

top_button_d = ttk.Button(master=top_frame_d, text='START')
top_button_d.pack(side=RIGHT, padx=5, pady=5)

top_combobox_d = ttk.Combobox(
    master=top_frame_d, values=summoner_spells, state='readonly')
top_combobox_d.pack(side=RIGHT, padx=5, pady=5)
top_combobox_d.current(3)

top_frame_f = ttk.Frame(master=top_label_frame)
top_frame_f.pack(fill=BOTH, expand=YES)

top_label_f = ttk.Label(master=top_frame_f, text='Marque o Spell')
top_label_f.pack(side=LEFT, padx=5, pady=5)

top_button_f = ttk.Button(master=top_frame_f, text='START')
top_button_f.pack(side=RIGHT, padx=5, pady=5)

top_combobox_f = ttk.Combobox(
    master=top_frame_f, values=summoner_spells, state='readonly')
top_combobox_f.pack(side=RIGHT, padx=5, pady=5)
top_combobox_f.current(8)

notebook_tab.add(top_label_frame, text='TOP')

root.mainloop()
