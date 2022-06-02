import time
import ttkbootstrap as ttk
from ttkbootstrap.constants import BOTH, YES, LEFT, RIGHT

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
root = ttk.Window(iconphoto=None,
                  themename='vapor',
                  alpha=1,
                  minsize=(255, 105))

root.geometry('270x160+1085+50')
root.attributes('-topmost', True)
root.overrideredirect(True)
root.minimized = False
root.maximized = False
app_name = 'Summoner Spell'

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
title_bar = ttk.Frame(root)

close_button = ttk.Button(title_bar, text='❌',
                          bootstyle=(ttk.DANGER, ttk.LINK),
                          command=root.destroy)

title_bar_title = ttk.Label(title_bar, text=app_name)

window = ttk.Frame(root)

title_bar.pack(fill=ttk.X)
close_button.pack(side=ttk.RIGHT)
title_bar_title.pack(side=ttk.LEFT, padx=10)

window.pack(expand=1, fill=ttk.BOTH)


def get_pos(event):
    if root.maximized is False:
        xwin = root.winfo_x()
        ywin = root.winfo_y()
        startx = event.x_root
        starty = event.y_root

        ywin = ywin - starty
        xwin = xwin - startx

        def move_window(event):
            root.geometry(f'+{event.x_root + xwin}+{event.y_root + ywin}')

        title_bar.bind('<B1-Motion>', move_window)
        title_bar.bind('<ButtonRelease-1>')
        title_bar_title.bind('<B1-Motion>', move_window)
        title_bar_title.bind('<ButtonRelease-1>')


title_bar.bind('<Button-1>', get_pos)
title_bar_title.bind('<Button-1>', get_pos)

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
summoner_spells = ['Barrier', 'Cleanse', 'Exhaust', 'Flash',
                   'Ghost',  'Heal', 'Ignite', 'Smite', 'Teleport']

cooldowns = {
    'Barrier': 180,
    'Cleanse': 210,
    'Exhaust': 210,
    'Flash': 300,
    'Ghost': 210,
    'Heal': 240,
    'Ignite': 180,
    'Smite': 15,
    'Teleport': 420,
}

roles = ['TOP', 'JNG', 'MID', 'ADC', 'SUP']

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

    button_d = ttk.Button(master=frame_d, text='START', command=countdown)
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

    button_f = ttk.Button(master=frame_f, text='START', command=countdown)
    button_f.pack(side=RIGHT, padx=5, pady=5)

    combobox_f = ttk.Combobox(
        master=frame_f, values=summoner_spells,
        state='readonly', exportselection=True)
    combobox_f.pack(side=RIGHT, padx=5, pady=5)
    combobox_f.current(8)
    print(combobox_f.get())

    notebook_tab.add(main_frame, text=set_lane)


def countdown(num_of_secs=300):
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = f'{m:02d}:{s:02d}'
        print(min_sec_format)
        time.sleep(1)
        num_of_secs -= 1
    print('Acabou!')


for role in roles:
    lanes(role)

root.mainloop()
