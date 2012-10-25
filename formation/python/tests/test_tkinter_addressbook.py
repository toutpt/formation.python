import unittest
from formation.python.tkinter.addressbook import tests

def suite():
    suite = unittest.TestSuite()
    suite.addTest(tests.test_addressbook())
    suite.addTest(WidgetTestCase('test_resize'))
    return suite