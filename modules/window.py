import ttkbootstrap as ttk
from ttkbootstrap.constants import BOTH, YES, LEFT, RIGHT, N
from modules.variables import summoner_spells, cooldowns


class MainWindow():
    def __init__(self, root) -> None:
        self.root = root

    def create_title_bar(self, app_name):
        self.root.attributes('-topmost', True)
        self.root.overrideredirect(True)
        self.root.minimized = False
        self.root.maximized = False

        self.title_bar = ttk.Frame(self.root)

        close_button = ttk.Button(self.title_bar, text='❌',
                                  bootstyle=(ttk.DANGER, ttk.LINK),
                                  command=self.root.destroy)

        title_bar_title = ttk.Label(self.title_bar, text=app_name)

        window = ttk.Frame(self.root)

        self.title_bar.pack(fill=ttk.X)
        close_button.pack(side=ttk.RIGHT)
        title_bar_title.pack(side=ttk.LEFT, padx=10)

        window.pack(expand=1, fill=ttk.BOTH)

        def get_pos(event):
            if self.root.maximized is False:
                xwin = self.root.winfo_x()
                ywin = self.root.winfo_y()
                startx = event.x_root
                starty = event.y_root

                ywin = ywin - starty
                xwin = xwin - startx

                def move_window(event):
                    self.root.geometry(
                        f'+{event.x_root + xwin}+{event.y_root + ywin}')

                self.title_bar.bind('<B1-Motion>', move_window)
                self.title_bar.bind('<ButtonRelease-1>')
                title_bar_title.bind('<B1-Motion>', move_window)
                title_bar_title.bind('<ButtonRelease-1>')

        self.title_bar.bind('<Button-1>', get_pos)
        title_bar_title.bind('<Button-1>', get_pos)

    def create_notebook(self):
        self.notebook_tab = ttk.Notebook(master=self.root)
        self.notebook_tab.pack(
            side=LEFT, padx=10, pady=10, expand=YES, fill=BOTH)

    def create_scale(self, min=0.4):
        self.scale = ttk.Scale(master=self.title_bar,
                               from_=min,
                               to=1.0,
                               value=1.0,
                               command=self.update_alpha,
                               orient='horizontal',
                               length=80, style='warning')
        self.scale.pack(anchor=N, padx=10, pady=10)

    def update_alpha(self, value):
        self.root.attributes('-alpha', self.scale.get())

    def create_tab(self, set_lane):
        self.theme_frame = ttk.Frame(master=self.root)
        self.theme_frame.pack(fill=BOTH,
                              expand=YES,
                              padx=5,
                              pady=5)

        self.frame_d = ttk.Frame(master=self.theme_frame)
        self.frame_d.pack(fill=BOTH,
                          expand=YES)

        self.theme_label = ttk.Label(master=self.frame_d,
                                     text='Marque o Spell')
        self.theme_label.pack(side=LEFT,
                              padx=5,
                              pady=5)

        self.button_d = ttk.Button(master=self.frame_d,
                                   text='✔️',
                                   bootstyle='light',
                                   command=self.countdown_d)
        self.button_d.pack(side=RIGHT,
                           padx=5,
                           pady=5)

        self.combobox_d = ttk.Combobox(master=self.frame_d,
                                       values=summoner_spells,
                                       state='readonly',
                                       exportselection=True,
                                       width=10)
        self.combobox_d.pack(side=RIGHT,
                             padx=5,
                             pady=5)
        self.combobox_d.current(3)

        self.frame_f = ttk.Frame(master=self.theme_frame)
        self.frame_f.pack(fill=BOTH,
                          expand=YES)

        self.label_f = ttk.Label(master=self.frame_f,
                                 text='Marque o Spell')
        self.label_f.pack(side=LEFT,
                          padx=5,
                          pady=5)

        self.button_f = ttk.Button(master=self.frame_f,
                                   text='✔️',
                                   bootstyle='light',
                                   command=self.countdown_f)
        self.button_f.pack(side=RIGHT,
                           padx=5,
                           pady=5)

        self.combobox_f = ttk.Combobox(master=self.frame_f,
                                       values=summoner_spells,
                                       state='readonly',
                                       exportselection=True,
                                       width=10)
        self.combobox_f.pack(side=RIGHT,
                             padx=5,
                             pady=5)
        self.combobox_f.current(8)

        self.notebook_tab.add(self.theme_frame,
                              text=set_lane)

    def countdown_d(self, validador=False, sec=None):
        value_d = self.combobox_d.get()
        self.time_cooldown = cooldowns.get(value_d)
        if validador is False:
            sec = int(self.time_cooldown)
        if sec == 0:
            self.theme_label.configure(text='Acabou o tempo!')
            self.button_d.configure(state='enable')
            self.button_d.configure(text='✔️')
        else:
            sec = sec - 1
            self.button_d.configure(state='disabled')
            self.button_d.configure(text='❌')
            self.theme_label.configure(text=f'Faltam: {sec}')
            self.theme_label.after(1000, lambda: self.countdown_d(True, sec))

    def countdown_f(self, validador=False, sec=None):
        value_f = self.combobox_f.get()
        self.time_cooldown = cooldowns.get(value_f)
        if validador is False:
            sec = int(self.time_cooldown)
        if sec == 0:
            self.label_f.configure(text='Acabou o tempo!')
            self.button_f.configure(state='enable')
            self.button_f.configure(text='✔️')
        else:
            sec = sec - 1
            self.button_f.configure(state='disabled')
            self.button_f.configure(text='❌')
            self.label_f.configure(text=f'Faltam: {sec}')
            self.label_f.after(1000, lambda: self.countdown_f(True, sec))

    def change_theme(self):
        self.theme_frame = ttk.Frame(master=self.root)
        self.theme_frame.pack(fill=BOTH,
                              expand=YES,
                              padx=5,
                              pady=5)

        self.theme_label = ttk.Label(master=self.theme_frame,
                                     text='Selecione um tema:')
        self.theme_label.pack(side=LEFT,
                              padx=5,
                              pady=5, expand=YES)

        style = ttk.Style()
        theme_names = style.theme_names()
        theme_cbo = ttk.Combobox(master=self.theme_frame,
                                 text=style.theme.name,
                                 state='readonly',
                                 height=50,
                                 values=theme_names,
                                 width=10)
        theme_cbo.pack(side=LEFT, padx=10, pady=10, expand=YES)
        theme_cbo.current(theme_names.index(style.theme.name))

        def change_theme(e):
            t = theme_cbo.get()
            style.theme_use(t)
            theme_cbo.selection_clear()

        theme_cbo.bind("<<ComboboxSelected>>", change_theme)

        self.notebook_tab.add(self.theme_frame,
                              text='Theme')
