
class Controller(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.bind()

    def bind(self):
        #lets bind quit on quit
        self.view.buttons['quit']['command'] = self.quit
        self.view.buttons['add']['command'] = self.add
        #we need to load contact in the view

    def quit(self):
        self.view.quit()

    def add(self):
        #get arg
        info = self.view.get_contact_info()
        contact = self.model.create_contact(info['lastname'], info['firstname'])
        contact.phone = info['phone']
        self.model.add_contact(contact)
