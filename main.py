import ttkbootstrap as ttk
from modules.window import MainWindow
from modules.variables import roles
from modules.size_screen import x, y

# Configurando tamnho da tela
root = ttk.Window(themename='vapor')
length = 270
width = 170
root.geometry(f'{length}x{width}+{x-length}+{y-width}')

# Configurando as funcionalidades
window = MainWindow(root=root)
window.create_title_bar(app_name='Summoner Spell')
window.create_notebook()
window.create_scale()

for keys, values in roles.items():
    window.create_tab(set_lane=keys,
                      spell_d=values.get('value_d'),
                      spell_f=values.get('value_f'))

window.change_theme()

# Rodando a janela
root.mainloop()
