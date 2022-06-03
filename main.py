import ttkbootstrap as ttk
from modules.window import MainWindow

root = ttk.Window(iconphoto=None,
                  themename='vapor',
                  alpha=1)

root.geometry('270x170+1085+50')


window = MainWindow(root=root)
window.create_title_bar(app_name='Summoner Spell')
window.create_notebook()
window.create_scale()
window.create_tab(set_lane='TOP')

root.mainloop()
