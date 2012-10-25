import tkontact_view
import tkontact_model
import tkontact_controller

def main():

    #create sample data
    c1 = tkontact_model.Contact('FRANCOIS', 'JeanMichel')
    c2 = tkontact_model.Contact('RICHARD', 'Johan')
    c3 = tkontact_model.Contact('SABOUREAU', 'Marc')
    model = tkontact_model.AddressBook()
    model.add_contact(c1)
    model.add_contact(c2)
    model.add_contact(c3)

    #create the view
    root, view = tkontact_view.init()

    #create the controller
    controller = tkontact_controller.Controller(model, view)

    #launch !
    root.mainloop()

if __name__ == '__main__':
    main()
