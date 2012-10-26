import view
import model
import controller

def main():

    #create model instance
    mymodel = model.AddressBook()
    c1 = model.Contact("FRANCOIS", "JeanMichel")
    mymodel.add_contact(c1)
    #create the view instance
    root, myview = view.init()

    #create the controller instance
    mycontroller = controller.Controller(mymodel, myview)

    #launch !
    root.mainloop()

if __name__ == '__main__':
    main()
