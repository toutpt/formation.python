from Tkinter import *
import pprint
pp = pprint.PrettyPrinter()

class Application(Frame):
    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def say_hi(self):
        self.HI = Button(self, text="Hi !", command=self.quit)
        self.HI.pack({'side': "bottom"})

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})
#        self.say_hi()

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

        self.entrythingy = Entry()
        self.entrythingy.pack()

        # here is the application variable
        self.contents = StringVar()
        # set it to some value
        self.contents.set("this is a variable")
        # tell the entry widget to watch this variable
        self.entrythingy["textvariable"] = self.contents

        # and here we get a callback when the user hits return.
        # we will have the program print out the value of the
        # application variable when the user hits return
        self.entrythingy.bind('<Key-Return>',
                              self.print_contents)
        self.createWidgets()

    def print_contents(self, event):
        import pdb;pdb.set_trace()
        print "hi. contents of entry is now ---->", \
              self.contents.get()

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self, padx=150, pady=150)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.quit
#        self.hi_there.place(x=40, y=160)

        self.hi_there.pack({"side": "left"})


if __name__ == '__main__':
    root = Tk()
#    root.geometry("300x280+300+300")#    app = Application(master=root)
    app2 = App(master=root)
    app2.master.title("My Do-Nothing Application")
    app2.master.geometry("200x100")
    app2.mainloop()
#    app.mainloop()
    root.destroy()
