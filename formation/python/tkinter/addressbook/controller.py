
class Controller(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.bind()
        self.load_model_data()

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

    def load_model_data(self):
        contacts = []

        for contact in self.model.get_contacts():
            contacts.append(contact.toString())

        self.view.add_contacts(contacts)
