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
    style.theme_create("st_app", parent="alt", settings={
        ".": {"configure": {"background": StColors.dark_grey,
                            "foreground": StColors.light_blue,
                            "relief": "flat",
                            "highlightcolor": StColors.bright_blue}},

        "TLabel": {"configure": {"foreground": StColors.dark_blue,
                                 "padding": 10,
                                 "font": ("Calibri", 12)}},

        "TNotebook": {"configure": {"padding": 5}},
        "TNotebook.Tab": {"configure": {"padding": [25, 5],
                                        "foreground": "white"},
                          "map": {"background": [("selected", StColors.mid_grey)],
                                  "expand": [("selected", [1, 1, 1, 0])]}},

        "TCombobox": {"configure": {"selectbackground": StColors.dark_grey,
                                    "fieldbackground": "white",
                                    "background": StColors.light_grey,
                                    "foreground": "black"}},

        "TButton": {"configure": {"font": ("Calibri", 13, 'bold'),
                                  "background": "black",
                                  "foreground": StColors.light_blue},
                    "map": {"background": [("active", StColors.bright_blue)],
                            "foreground": [("active", 'black')]}},

        "TEntry": {"configure": {"foreground": "black"}},
        "Horizontal.TProgressbar": {"configure": {"background": StColors.mid_grey}}
    })
    style.theme_use("st_app")