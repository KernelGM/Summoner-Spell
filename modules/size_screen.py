import ctypes

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

x = screensize[0]
y = screensize[1]

length = 270
width = 170

nw = f'{x-length}+{y-width}'
se = f'{x-length}+{y-y}'
