import ttkbootstrap as ttk
from modules.window import MainWindow


root = ttk.Window(iconphoto=None,
                  themename='vapor',
                  alpha=1,
                  minsize=(255, 105))

root.geometry('270x160+1085+50')


window = MainWindow(root=root)
window.create_title_bar(app_name='Summoner Spell')
window.create_notebook()
window.create_tab(set_lane='TOP')

root.mainloop()
