import ttkbootstrap as ttk
from ttkbootstrap.constants import BOTH, YES, LEFT, RIGHT, N
from modules.variables import summoner_spells, cooldowns
from keyboard import write, press_and_release
from time import sleep


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
        def countdown_d(validador=False, sec=None):
            value_d = combobox_d.get()
            time_cooldown = cooldowns.get(value_d)
            if validador is False:
                sec = int(time_cooldown)
            if sec == 0:
                label_d.configure(text='Acabou o tempo!')
                button_d.configure(state='enable')
                button_d.configure(text='✔️')
                self.warning_timeout()
            else:
                sec = sec - 1
                button_d.configure(state='disabled')
                button_d.configure(text='❌')
                label_d.configure(text=f'Faltam: {sec} seg')
                label_d.after(1000, lambda: countdown_d(True, sec))

        def countdown_f(validador=False, sec=None):
            value_f = combobox_f.get()
            time_cooldown = cooldowns.get(value_f)
            if validador is False:
                sec = int(time_cooldown)
            if sec == 0:
                label_f.configure(text='Acabou o tempo!')
                button_f.configure(state='enable')
                button_f.configure(text='✔️')
                self.warning_timeout()
            else:
                sec = sec - 1
                button_f.configure(state='disabled')
                button_f.configure(text='❌')
                label_f.configure(text=f'Faltam: {sec} seg')
                label_f.after(1000, lambda: countdown_f(True, sec))

        main_frame = ttk.Frame(master=self.root)
        main_frame.pack(fill=BOTH,
                        expand=YES,
                        padx=5,
                        pady=5)

        frame_d = ttk.Frame(master=main_frame)
        frame_d.pack(fill=BOTH,
                     expand=YES)

        label_d = ttk.Label(master=frame_d,
                            text='Marque o Spell')
        label_d.pack(side=LEFT,
                     padx=5,
                     pady=5)

        button_d = ttk.Button(master=frame_d,
                              text='✔️',
                              bootstyle='light',
                              command=countdown_d)
        button_d.pack(side=RIGHT,
                      padx=5,
                      pady=5)

        combobox_d = ttk.Combobox(master=frame_d,
                                  values=summoner_spells,
                                  state='readonly',
                                  exportselection=True,
                                  width=10)
        combobox_d.pack(side=RIGHT,
                        padx=5,
                        pady=5)
        combobox_d.current(3)

        frame_f = ttk.Frame(master=main_frame)
        frame_f.pack(fill=BOTH,
                     expand=YES)

        label_f = ttk.Label(master=frame_f,
                            text='Marque o Spell')
        label_f.pack(side=LEFT,
                     padx=5,
                     pady=5)

        button_f = ttk.Button(master=frame_f,
                              text='✔️',
                              bootstyle='light',
                              command=countdown_f)
        button_f.pack(side=RIGHT,
                      padx=5,
                      pady=5)

        combobox_f = ttk.Combobox(master=frame_f,
                                  values=summoner_spells,
                                  state='readonly',
                                  exportselection=True,
                                  width=10)
        combobox_f.pack(side=RIGHT,
                        padx=5,
                        pady=5)
        combobox_f.current(8)

        self.notebook_tab.add(main_frame,
                              text=set_lane)

    def change_theme(self):
        self.theme_frame = ttk.Frame(master=self.root)
        self.theme_frame.pack(fill=BOTH, expand=YES, padx=5, pady=5)

        self.theme_label = ttk.Label(
            master=self.theme_frame, text='Selecione um tema:')
        self.theme_label.pack(side=LEFT, padx=5, pady=5, expand=YES)

        self.style = ttk.Style()
        self.theme_names = self.style.theme_names()
        self.theme_cbo = ttk.Combobox(master=self.theme_frame,
                                      text=self.style.theme.name,
                                      state='readonly',
                                      height=50,
                                      values=self.theme_names,
                                      width=10)

        self.theme_cbo.pack(side=LEFT, padx=10, pady=10, expand=YES)
        self.theme_cbo.current(self.theme_names.index(self.style.theme.name))

        def change_theme(e):
            t = self.theme_cbo.get()
            self.style.theme_use(t)
            self.theme_cbo.selection_clear()

        self.theme_cbo.bind("<<ComboboxSelected>>", change_theme)

        self.notebook_tab.add(self.theme_frame, text='Theme')

    def warning_timeout(self):
        press_and_release('enter')
        sleep(1)
        write('olá mundo')
        press_and_release('enter')
