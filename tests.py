import unittest
from unittest.mock import patch
from lib import getById,getByName,add,update,delete
import sqlite3

class TestIfValidGetByIdMethod(unittest.TestCase):

    def test_getid(self):

        self.assertEqual(getById("1"),(1,"egor","2"))
        self.assertEqual(getById("2"),(2,"eg","eg"))

class TestIfValidGetByNameMethod(unittest.TestCase):

    def test_gebyname(self):

        self.assertEqual(getByName("eg"),("eg"))
        self.assertEqual(getByName("egor"),("2"))

class TestIfValidAddMethod(unittest.TestCase):

    def test_add(self):

        self.assertEqual(add("jeka","privet"),("Success"))
        self.assertEqual(add("jekosik",""),("Message cant be empty"))

class TestIfValidUpdateMethod(unittest.TestCase):

    def test_update(self):
        self.assertEqual(update(92939,"Ssss"),("Theres no user with such an ID"))
        self.assertEqual(update(1,"hi"),("Success"))

class TestIfValidDeleteMethod(unittest.TestCase):

    def test_delete(self):
        self.assertEqual(delete(92939),(None))
        self.assertEqual(delete(5),("Success"))





if __name__ == '__main__':
    unittest.main()