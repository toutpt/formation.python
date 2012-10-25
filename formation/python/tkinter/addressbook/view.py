from Tkinter import *
from ttk import Frame, Button, Label, Style
from ttk import Entry


class TKontactFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.next_row = 0
        self.fields = {}
        self.buttons = {}
        self.initUI()

    def initUI(self):
        self.parent.title("TKontact")
        self.style = Style()
        self.style.theme_use("default")

#        frame = Frame(self, relief=RAISED, borderwidth=1)
#        frame.pack(fill=BOTH, expand=1)

#        self.pack(fill=BOTH, expand=1)

        self.frame_left = Frame(self)
        self.frame_left.grid(row=0, column=0)
        self.frame_right = Frame(self)
        self.frame_right.grid(row=0, column=1)

        self.add_field("lastname")
        self.add_field("firstname")
        self.add_field("phone")
        self.add_button("add")
        self.add_button("delete")
        self.add_button("search")
        self.add_button("quit")

        self.add_contactlist()
        self.pack()

    def add_field(self, name):
        self.fields[name] = {'label': Label(self.frame_right,
                                            text=name),
                            'entry': Entry(self.frame_right)}
        self.fields[name]['label'].grid(row=self.next_row, column=1)
        self.next_row += 1
        self.fields[name]['entry'].grid(row=self.next_row, column=1)
        self.next_row += 1

    def add_button(self, name):
        self.buttons[name] = Button(self.frame_right, text=name)
        self.buttons[name].grid(row=self.next_row, column=1)
        self.next_row+=1

    def add_contactlist(self):
        text = Listbox(self.frame_left)
        text.grid(row=0, column=0, sticky=E+W+S+N)

    def get_contact_info(self):
        info = {'lastname': None,
                'firstname': None,
                'phone': None}
        for key in info:
            info[key] = self.fields[key]['entry'].get()
        return info

def init():
    root = Tk()
    app = TKontactFrame(root)
    return root, app
