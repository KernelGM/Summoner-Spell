import ttkbootstrap as ttk
from ttkbootstrap.constants import BOTH

root = ttk.Window(themename='vapor')
root.geometry('200x400')

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
top_frame = ttk.Labelframe(root, text='Top Lane', bootstyle="info")
top_frame.pack(fill=BOTH, expand=True)

top_spell_d = ttk.Label(top_frame, text='1. This is a Label.')
top_spell_d.pack(fill=BOTH, expand=True)

top_spell_f = ttk.Label(top_frame, text='2. This is another Label.')
top_spell_f.pack(fill=BOTH, expand=True)

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
jg_frame = ttk.Labelframe(root, text='Jungler')
jg_frame.pack(fill=BOTH, expand=True)

jg_spell_d = ttk.Label(jg_frame, text='1. This is a Label.')
jg_spell_d.pack(fill=BOTH, expand=True)

jg_spell_f = ttk.Label(jg_frame, text='2. This is another Label.')
jg_spell_f.pack(fill=BOTH, expand=True)

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
mid_frame = ttk.Labelframe(root, text='Mid Lane')
mid_frame.pack(fill=BOTH, expand=True)

mid_spell_d = ttk.Label(mid_frame, text='1. This is a Label.')
mid_spell_d.pack(fill=BOTH, expand=True)

mid_spell_f = ttk.Label(mid_frame, text='2. This is another Label.')
mid_spell_f.pack(fill=BOTH, expand=True)

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
adc_frame = ttk.Labelframe(root, text='AD Carry')
adc_frame.pack(fill=BOTH, expand=True)

adc_spell_d = ttk.Label(adc_frame, text='1. This is a Label.')
adc_spell_d.pack(fill=BOTH, expand=True)

adc_spell_f = ttk.Label(adc_frame, text='2. This is another Label.')
adc_spell_f.pack(fill=BOTH, expand=True)

# -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
sup_frame = ttk.Labelframe(root, text='Support')
sup_frame.pack(fill=BOTH, expand=True)

sup_spell_d = ttk.Label(sup_frame, text='1. This is a Label.')
sup_spell_d.pack(fill=BOTH, expand=True)

sup_spell_f = ttk.Label(sup_frame, text='2. This is another Label.')
sup_spell_f.pack(fill=BOTH, expand=True)


root.mainloop()
