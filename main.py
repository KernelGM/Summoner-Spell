import ttkbootstrap as ttk
from modules.window import MainWindow
from modules.variables import roles

# Configurando tamnho da tela
root = ttk.Window(themename='vapor')
root.geometry('270x170+1085+50')

# Configurando as funcionalidades
window = MainWindow(root=root)
window.create_title_bar(app_name='Summoner Spell')
window.create_notebook()
window.create_scale()
for role in roles:
    window.create_tab(set_lane=role)
window.change_theme()

# Rodando a janela
root.mainloop()
