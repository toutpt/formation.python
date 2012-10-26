import os
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

    def __init__(self, filename=None):
        self.contacts = {}
        self.filename = filename
        if not self.filename:
            self.filename = "carnet.txt"

    def add_contact(self, contact):
        """Add a contact to the address book."""
        self.contacts[contact.id] = contact
        print "contact added: %s"% contact.toString()
    
    def del_contact(self, contactid):
        """delete a contact from a given contact id"""
        del self.contacts[contactid]

    def search(self, term):
        """Search a contact from term 'term'
        -> [contact1, contact2, ...]
        """
        contacts = []
        for contact in self.contacts.values():
            if term.lower() in contact.lastname.lower() \
            or term.lower() in contact.firstname.lower():
                contacts.append(contact)
        return contacts

    def create_contact(self, lastname, firstname):
        """-> instance Contact"""
        return Contact(lastname, firstname)

    def get_contacts(self):
        return self.contacts.values()

    def get_file(self):
        exists = os.path.exists(self.filename)
        if exists and not os.path.isfile(self.filename):
            raise ValueError('the argument filename must be a file')
        if exists:
            mode = "rw+"
        else:
            mode = "w+"
        return open(self.filename, mode)

    def read(self):
        f = self.get_file()
        for line in f:
            tokens = line.split(';')
            if len(tokens) >= 4:
                contact = self.create_contact(tokens[1], tokens[2])
                contact.id = tokens[0]
            if len(tokens) == 5:
                contact.phone = tokens[3]
            self.add_contact(contact)
        f.close()

    def write(self):
        f = file(self.filename, 'w+')
        contents = ""
        for contact in self.contacts.values():
            contents += "%s;%s;%s;%s%s" % (contact.id,
                                           contact.lastname,
                                           contact.firstname,
                                           contact.phone or "",
                                           os.linesep)
        f.write(contents.encode('utf-8'))
        f.close()

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