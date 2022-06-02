import ttkbootstrap as ttk


def title_bar(app_name, root):
    root.attributes('-topmost', True)
    root.overrideredirect(True)
    root.minimized = False
    root.maximized = False

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
