from tkinter import *
from tkinter.filedialog import *
from tkinter import colorchooser

class Sticky:

    def __init__(self):
        self.bg_color = 'yellow'
        self.font = 'Helvetica'
        self.text_size = 24

        self.window = Tk()
        self.window.geometry('640x480')
        self.window.minsize(320,240)
        self.window.maxsize(1280,720)
        self.window.title('Sticky')

        self.menu_bar = Menu(self.window)

        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label='New', command=self.new_sticky)
        self.menu_bar.add_cascade(label='File', menu=self.file_menu)

        self.options_menu = Menu(self.menu_bar, tearoff=0)
        self.options_menu.add_command(label='Font', command=self.change_font)
        self.options_menu.add_command(label='Text size', command=self.change_textsize)
        self.options_menu.add_command(label='Background', command=self.change_background)
        self.menu_bar.add_cascade(label='Options', menu=self.options_menu)

        self.view_menu = Menu(self.menu_bar, tearoff=0)
        self.view_menu.add_command(label='View toolbar [Ctrl+T]', command=self.view_toolbar)
        self.menu_bar.add_cascade(label='View', menu=self.view_menu)

        self.text = Text(self.window, width=640, height=480)
        self.text.config(font=(self.font, self.text_size))
        self.text.pack()
        self.text.config(background='yellow')

        self.toolbar_visible = True
        self.window.config(menu=self.menu_bar)

        self.first_keycode = None
        self.second_keycode = None
        self.window.bind("<KeyPress>", self.key_pressed)

    def change_font(self):
        font_window = Toplevel(self.window)
        font_window.geometry('200x500')
        listbox = Listbox(font_window, width=200, height=500)
        listbox.insert(1,'Times New Roman')
        listbox.insert(2,'Impact')
        listbox.insert(3,'Arial')
        listbox.pack()
        
        def on_click(event):
            selection = event.widget.curselection()
            if selection:
                index = selection[0]
                data = event.widget.get(index)
                global font
                font = data
                self.text.config(font=(font, self.text_size))
            else:
                print('All text was selected')

        listbox.bind('<<ListboxSelect>>', on_click)

    def change_textsize(self):
        font_window = Toplevel(self.window)
        font_window.geometry('200x500')
        textsize_listbox = Listbox(font_window, width=200, height=500)
        for i in range(50):
            textsize_listbox.insert(i, str(i))
        textsize_listbox.pack()
        
        def on_click2(event):
            selection = event.widget.curselection()
            if selection:
                index = selection[0]
                data = event.widget.get(index)
                textsize = data
                self.text.config(font=(self.font, textsize))
            else:
                print('All text was selected')

        textsize_listbox.bind('<<ListboxSelect>>', on_click2)

    def change_background(self):
        color_code = colorchooser.askcolor(title='Choose color')  
        background_color = color_code[1]
        self.text.config(background=background_color)

    def new_sticky(self):
        clone = Sticky()
        clone.loop()

    def view_toolbar(self):
        print(self.toolbar_visible)
        if(self.toolbar_visible == True):
            self.toolbar_visible = False
            self.window.config(menu='')
        else:
            self.toolbar_visible = True
            self.window.config(menu=self.menu_bar)

    def key_pressed(self, event):
        if(self.first_keycode == 17 and event.keycode == 84):
            self.view_toolbar()
        else:
            self.first_keycode=event.keycode

    def loop(self):
        self.window.mainloop()

sticky = Sticky()
sticky.loop()