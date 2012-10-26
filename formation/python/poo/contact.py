
class Contact(object):
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname
        self.phone = None

if __name__ == "__main__":
    contact1 = Contact("FRANCOIS" , "Jean-Michel")
    contact1.phone = ["00 00 00 00 00"]
    print contact1
