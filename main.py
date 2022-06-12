import ttkbootstrap as ttk
from modules.variables import roles
from modules.size_screen import length, width, se
from modules.window import MainWindow

# Configurando tamnho da tela
root = ttk.Window(themename='vapor')
root.geometry(f'{length}x{width}+{se}')

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

# Cria janela na taskbar do Windows
root.wm_title('Summoner Spell')
root.after(10, lambda: window.create_appwindow(root))

# Rodando a janela
root.mainloop()
