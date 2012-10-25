import uuid

class Contact(object):
    def __init__(self, lastname, firstname):
        self.id = uuid.uuid4()
        self.lastname = lastname
        self.firstname = firstname
        self.phone = None

    def toString(self):
        return "%s %s"% (self.firstname, self.lastname)


class AddressBook(object):

    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        self.contacts[contact.id] = contact
        print "contact added: %s"% contact.toString()
    
    def del_contact(self, contactid):
        del self.contacts[contactid]

    def search(self, term):
        contacts = []
        for contact in self.contacts:
            if term in contact.lastname or term in contact.firstname:
                contacts.append(contact)
        return contacts

if __name__ == '__main__':
    c1 = Contact('FRANCOIS', 'JeanMichel')
    c2 = Contact('RICHARD', 'Johan')
    c3 = Contact('SABOUREAU', 'Marc')
    a = AddressBook()
    a.add_contact(c1)
    a.add_contact(c2)
    a.add_contact(c3)
    if len(a.contacts) !=3:
        print "there is a pb"