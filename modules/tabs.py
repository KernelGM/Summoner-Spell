import ttkbootstrap as ttk
from ttkbootstrap.constants import BOTH, YES, LEFT, RIGHT
from modules.variables import summoner_spells


def tab(root, set_lane, notebook_tab):

    main_frame = ttk.Frame(master=root)
    main_frame.pack(fill=BOTH, expand=YES, padx=5, pady=5)

    frame_d = ttk.Frame(master=main_frame)
    frame_d.pack(fill=BOTH, expand=YES)

    label_d = ttk.Label(master=frame_d, text='Marque o Spell')
    label_d.pack(side=LEFT, padx=5, pady=5)

    button_d = ttk.Button(master=frame_d, text='START', command='')
    button_d.pack(side=RIGHT, padx=5, pady=5)

    combobox_d = ttk.Combobox(
        master=frame_d, values=summoner_spells,
        state='readonly', exportselection=True)
    combobox_d.pack(side=RIGHT, padx=5, pady=5)
    combobox_d.current(3)

    frame_f = ttk.Frame(master=main_frame)
    frame_f.pack(fill=BOTH, expand=YES)

    label_f = ttk.Label(master=frame_f, text='Marque o Spell')
    label_f.pack(side=LEFT, padx=5, pady=5)

    button_f = ttk.Button(master=frame_f, text='START', command='')
    button_f.pack(side=RIGHT, padx=5, pady=5)

    combobox_f = ttk.Combobox(
        master=frame_f, values=summoner_spells,
        state='readonly', exportselection=True)
    combobox_f.pack(side=RIGHT, padx=5, pady=5)
    combobox_f.current(8)

    notebook_tab.add(main_frame, text=set_lane)
