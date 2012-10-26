
class Controller(object):
    def __init__(self, model, view):
        self.model = model
        self.model.read()
        self.view = view

        self.bind()
        self.refresh()

    def bind(self):
        #lets bind quit on quit
        self.view.buttons['quit']['command'] = self.quit
        self.view.buttons['add']['command'] = self.add
        self.view.buttons['search']['command'] = self.search
        self.view.buttons['delete']['command'] = self.delete
        self.view.buttons['open']['command'] = self.open
        self.view.contacts_box.bind("<<ListboxSelect>>", self.click_listbox)
        #we need to load contact in the view

    def get_selected_contact(self):
        selection = self.view.contacts_box.curselection()
        if not selection:
            print "il n y a pas de selection"
            return

        #recuperer id contact (passer par index list)
        index = int(selection[0])
        contact = self.model.get_contacts()[index]
        return contact

    def click_listbox(self, event):
        c = self.get_selected_contact()
        info = {'lastname': c.lastname,
                'firstname': c.firstname,
                'phone': c.phone or ''}
        self.view.set_contact_info(info)

    def search(self):
        self.view.empty()

        term = self.view.fields['search']['entry'].get()
        results = []
        contacts = self.model.search(term)

        for contact in contacts:
            results.append(contact.toString())

        self.view.add_contacts(results)

    def delete(self):
        contact = self.get_selected_contact()
        #check selection listbox
        contactid = contact.id

        #delete contact dans le model
        self.model.del_contact(contactid)
        self.refresh()

    def quit(self):
        self.view.quit()
        self.model.write()

    def add(self):
        #get arg
        info = self.view.get_contact_info()
        contact = self.model.create_contact(info['lastname'], info['firstname'])
        contact.phone = info['phone']
        self.model.add_contact(contact)
        self.refresh()

    def refresh(self):
        """Refresh the UI from the data"""
        self.view.empty()
        contacts = []

        for contact in self.model.get_contacts():
            contacts.append(contact.toString())

        self.view.add_contacts(contacts)

    def open(self):
        """open a new window"""
        contact = self.get_selected_contact()
        view = self.view.open_contact_window()
        controller = ControllerContact(contact, view)


class ControllerContact(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view
