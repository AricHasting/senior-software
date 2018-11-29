from tkinter import ttk


class StColors(object):
    dark_blue = '#5c85d6'
    bright_blue = '#66ccff'
    dark_grey    = '#666666'
    mid_grey     = '#999999'
    light_grey   = '#c8c8c8'
    light_blue = '#cce6ff'

def set_app_style():
    style = ttk.Style()
    style = ttk.Style()
    style.configure(".", background=StColors.dark_grey, foreground=StColors.light_blue,
                    relief="flat", highlightcolor=StColors.bright_blue)
    style.configure("TLabel", foreground=StColors.dark_blue, padding=10, font=("Calibri", 12))
    style.configure("TNotebook", padding=5)
    style.configure("TNotebook.Tab", padding=[25, 5], foreground="white")
    style.map("TNotebook.Tab", background=[("selected", StColors.mid_grey)], expand=[("selected", [1, 1, 1, 0])])
    style.configure("TCombobox", selectbackground=StColors.dark_grey, fieldbackground="white",
                    background=StColors.light_grey, foreground=StColors.dark_blue)
    style.configure("TButton", font=("Calibri", 13, 'bold'), background="black", foreground=StColors.light_blue)
    style.map("TButton", background=[("active", StColors.bright_blue)], foreground=[("active", StColors.dark_blue)])
    style.configure("TEntry", foreground=StColors.dark_blue)
    style.configure("Horizontal.TProgressbar", background=StColors.mid_grey)

    style.theme_use("st_app")