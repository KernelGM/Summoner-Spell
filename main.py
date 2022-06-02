import ttkbootstrap as ttk
from ttkbootstrap.constants import BOTH, YES, X, NW, NE, LEFT, RIGHT, TOP, BOTTOM, N, E, S, SW, SE, W

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
root = ttk.Window(title='Summoner Spell',
                  iconphoto=None,
                  themename='superhero',
                  alpha=1,
                  minsize=(100, 200))
root.geometry('270x400+1090+50')
root.attributes('-topmost', True)

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
summoner_spells = sorted(['Heal', 'Ghost', 'Barrier', 'Exhaust',
                          'Flash', 'Teleport', 'Smite', 'Cleanse', 'Ignite'])

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
top_label_frame = ttk.Labelframe(master=root, text='Top Lane')
top_label_frame.pack(fill=BOTH, expand=YES, padx=5, pady=3)

top_frame_d = ttk.Frame(master=top_label_frame)
top_frame_d.pack(fill=BOTH, expand=YES)

top_label_d = ttk.Label(master=top_frame_d, text='Marque o Spell [D]')
top_label_d.pack(side=LEFT, padx=5, pady=5)

top_button_d = ttk.Button(master=top_frame_d, text='START')
top_button_d.pack(side=RIGHT, padx=5, pady=5)

top_combobox_d = ttk.Combobox(
    master=top_frame_d, values=summoner_spells, state='readonly')
top_combobox_d.pack(side=RIGHT, padx=5, pady=5)

top_frame_f = ttk.Frame(master=top_label_frame)
top_frame_f.pack(fill=BOTH, expand=YES)

top_label_f = ttk.Label(master=top_frame_f, text='Marque o Spell [F]')
top_label_f.pack(side=LEFT, padx=5, pady=5)

top_button_f = ttk.Button(master=top_frame_f, text='START')
top_button_f.pack(side=RIGHT, padx=5, pady=5)

top_combobox_f = ttk.Combobox(
    master=top_frame_f, values=summoner_spells, state='readonly')
top_combobox_f.pack(side=RIGHT, padx=5, pady=5)


# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
jg_frame = ttk.Labelframe(root, text='Jungler')
jg_frame.pack(fill=BOTH, expand=YES, padx=5, pady=5)

jg_spell_d = ttk.Label(jg_frame, text='1. This is a Label.')
jg_spell_d.pack(fill=BOTH, expand=YES)

jg_spell_f = ttk.Label(jg_frame, text='2. This is another Label.')
jg_spell_f.pack(fill=BOTH, expand=YES)

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
mid_frame = ttk.Labelframe(root, text='Mid Lane')
mid_frame.pack(fill=BOTH, expand=YES, padx=5, pady=5)

mid_spell_d = ttk.Label(mid_frame, text='1. This is a Label.')
mid_spell_d.pack(fill=BOTH, expand=YES)

mid_spell_f = ttk.Label(mid_frame, text='2. This is another Label.')
mid_spell_f.pack(fill=BOTH, expand=YES)

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
adc_frame = ttk.Labelframe(root, text='AD Carry')
adc_frame.pack(fill=BOTH, expand=YES, padx=5, pady=5)

adc_spell_d = ttk.Label(adc_frame, text='1. This is a Label.')
adc_spell_d.pack(fill=BOTH, expand=YES)

adc_spell_f = ttk.Label(adc_frame, text='2. This is another Label.')
adc_spell_f.pack(fill=BOTH, expand=YES)

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
sup_frame = ttk.Labelframe(root, text='Support')
sup_frame.pack(fill=BOTH, expand=YES, padx=5, pady=5)

sup_spell_d = ttk.Label(sup_frame, text='1. This is a Label.')
sup_spell_d.pack(fill=BOTH, expand=YES)

sup_spell_f = ttk.Label(sup_frame, text='2. This is another Label.')
sup_spell_f.pack(fill=BOTH, expand=YES)


root.mainloop()
