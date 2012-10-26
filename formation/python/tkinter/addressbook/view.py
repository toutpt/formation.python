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
        self.contacts_box = None
        self.contact_frame = None

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
        self.add_button("open")
        self.add_button("delete")
        self.add_field("search")
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
        self.contacts_box = Listbox(self.frame_left)
        self.contacts_box.grid(row=0, column=0, sticky=E+W+S+N)

    def get_contact_info(self):
        info = {'lastname': None,
                'firstname': None,
                'phone': None}
        for key in info:
            info[key] = self.fields[key]['entry'].get()
        return info
    def set_contact_info(self, info):
        for key in info:
            self.fields[key]['entry'].delete(0, END)
            self.fields[key]['entry'].insert(END, info[key])

    def add_contacts(self, list_contacts_str):
        for contact in list_contacts_str:
            self.contacts_box.insert(END, contact)

    def empty(self):
        self.contacts_box.delete(0, END)
        for field in ('lastname', 'firstname', 'phone'):
            self.fields[field]['entry'].delete(0, END)

    #experimental !!!!
    def open_contact_window(self):
        self.contact_frame = ContactFrame(self.parent)
        self.dropUI()
        self.contact_frame.pack()

    def dropUI(self):
        self.frame_left.destroy()
        self.frame_right.destroy()
        self.destroy()
#        self.__init__(self.parent)

#        for field in self.fields:
#            self.fields[field]['entry'].destroy()
#            self.fields[field]['label'].destroy()
#        for button in self.buttons:
#            self.buttons[button].destroy()
#        self.contacts_box.destroy()

class ContactFrame(TKontactFrame):
    def __init__(self, parent):
        TKontactFrame.__init__(self, parent)

    def initUI(self):
        self.style = Style()
        self.style.theme_use("default")
        self.add_button("test")
        self.add_button("test2")
        self.add_button("test3")
        self.add_button("test4")

    def add_button(self, name):
        self.buttons[name] = Button(self, text=name)
        self.buttons[name].grid(row=self.next_row, column=1)
        self.next_row+=1


def init():
    root = Tk()
    app = TKontactFrame(root)
    return root, app
