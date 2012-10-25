#-*- coding: utf-8 -*-

addressbook = {}


def add_contact(firstname, lastname, phone=None):
    contact = {'lastname': lastname,
               'firstname': firstname}
    if phone:
        contact['phone'] = [phone]
    found = False
    index = lastname[0]
    if index in addressbook:
        for someone in addressbook[index]:
            if someone['lastname'] == contact['lastname'] and \
               someone['firstname'] == contact['firstname']:
                found = True
                if phone not in someone['phone']:
                    someone['phone'].append(phone)
        if not found:
            addressbook[index].append(contact)
    else:
        addressbook[index] = [contact]


if __name__ == "__main__":
    import pprint

    add_contact('Marc', 'Saboureau', phone= "06 06 06 06 06")
    add_contact('Marc', 'Saboureau', phone= "02 40 04 04 04")
    add_contact('Jean-Michel', 'François', phone="06 75 55 15 55")
    add_contact('Thierry', 'François', phone="06 75 55 15 56")
    pp = pprint.PrettyPrinter()
    pp.pprint(addressbook)
