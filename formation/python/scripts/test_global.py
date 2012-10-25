global globvar    # Needed to modify global copy of globvar
globvar = 0

def set_globvar_to_one():
    #global globvar    # Needed to modify global copy of globvar
    globvar = 1

def print_globvar():
    """madoc"""
    print globvar     # No need for global declaration to read value of globvar

set_globvar_to_one()
print_globvar()       # Prints 1
print print_globvar.__doc__
import pdb;pdb.set_trace()