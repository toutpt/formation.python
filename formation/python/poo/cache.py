
class Private(object):
    pass

class MonSuperCalcul(object):

    def __init__(self):
        self._cache = {}
        self._value = None

    def ma_methode(self, arg):
        if arg in self._cache:
            return self._cache[arg]
        #....
        print "execute"
        rez = "super resultat %s" % arg

        self._cache[arg] = rez

        return rez

    @property
    def moyenne(self):
        return "moyenne"

    def get_value(self):
        if type(self._value) == int:
            return self._value

    def set_value(self, value):
        if type(value) == int:
            self._value = value
    value = property(get_value, set_value)

__all__ = ['MonSuperCalcul']

if __name__=='__main__':
    calc = MonSuperCalcul()
    calc.ma_methode("toto")
    calc.ma_methode("titi")
    calc.ma_methode("toto")
    print "initial value: %s" % calc.value
    calc.value = "toto"
    print "is value == 'toto' ? -> %s" % calc.value
    calc._value = "toto"
    print "is value == 'toto' ? -> %s" % calc.value
    
    calc.value = 10
    print "is value == 10 ? -> %s" % calc.value
    