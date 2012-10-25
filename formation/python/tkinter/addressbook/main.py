import view
import model
import controller

def main():

    #create model instance
    model = model.AddressBook()

    #create the view instance
    root, view = view.init()

    #create the controller instance
    controller = controller.Controller(model, view)

    #launch !
    root.mainloop()

if __name__ == '__main__':
    main()
