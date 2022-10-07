#!/usr/bin/python3
"Unit tests for Rectangle class"
import unittest
from unittest import mock
import io
import os
from models.square import Square
from models.base import Base
import json
import sys

class TestSquare(unittest.TestCase):
    """Testing Square"""

    def test_instance(self):
        """test input size correct standard """

        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

        with self.assertRaises(TypeError):
            Square(5, "1")

        with self.assertRaises(TypeError):
            Square()

        with self.assertRaises(TypeError):
            Square("1")

        with self.assertRaises(ValueError):
            Square(-5, 3, 4)

        with self.assertRaises(TypeError):
            Square(1, 2, "3")

        with self.assertRaises(ValueError):
            Square(1, -2)

        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_dictionary(self):
        s1 = Square(10, 2, 1, 1)
        s1_dict = s1.to_dictionary()
        self.assertEqual(s1_dict, {'id': 1, 'x': 2, 'size': 10, 'y': 1})

    def test_case_normal(self):
        """Test of Square(1, 2, 3, 4) exists"""
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.id, 4)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_load_from_file(self):
        """Test of Square.save_to_file(None) in Square exists"""
        Square.save_to_file(None)
        self.assertTrue(os.path.isfile('Square.json'))

        load_file = Square.load_from_file()
        self.assertEqual(len(load_file), 0)

        """Test of Square.save_to_file([]) in Square exists"""

    def test_area(self):
        """testing area"""
        s = Square(5)
        self.assertEqual(s.area(), 25)

        s = Square(1, 2)
        self.assertEqual(s.area(), 1)

    def test_display(self):
        """test display()"""
        s = Square(5)
        with mock.patch("sys.stdout", new=io.StringIO()) as mock_stdout:
            s.display()

        assert mock_stdout.getvalue() == "#####\n#####\n#####\n#####\n#####\n"

        s = Square(1, 2)
        with mock.patch("sys.stdout", new=io.StringIO()) as mock_stdout:
            s.display()

        assert mock_stdout.getvalue() == "  #\n"

    def test_string(self):
        """Test str"""
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.__str__(), '[Square] (4) 2/3 - 1')

    def test_update(self):
        """test update()"""
        s1 = Square(2)
        s1.update(10)
        self.assertEqual(s1.id, 10)

        s1.update(size=1, id=89, x=2)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.x, 2)

    def test_created(self):
        """Test of Square.create(**{ 'id': 89 }) in Square exists"""
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)

        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)

        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)

        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)


    def test_to_dictionary(self):
        """ Test of to_dictionary() in Square exists """
        dict = {'id': 7, 'size': 10, 'x': 9, 'y': 8}
        s = Square(10, 9, 8, 7)
        self.assertEqual(dict, s.to_dictionary())

    def test_save_to_file(self):
        '''
            Testing saving a file into json format
        '''
        try:
            os.remove("Square.json")
        except:
            pass
        r1 = Square(5, 0, 0, 346)
        Square.save_to_file([r1])

        with open("Square.json", "r") as file:
            content = file.read()
        t = [{"id": 346, "x": 0, "size": 5, "y": 0}]
        self.assertEqual(t, json.loads(content))

    def test_save_to_file_no_iter(self):
        '''
            Sending a non iterable to the function
        '''
        with self.assertRaises(TypeError):
            Square.save_to_file(self)

    def test_save_to_file_None(self):
        '''
            Testing saving a file into json format sending None
        '''
#        try:
#            os.remove("Square.json")
#        except:
#            pass
        r1 = Square(5, 0, 0, 346)
        Square.save_to_file(None)

        with open("Square.json", "r") as file:
            content = file.read()

        self.assertEqual("[]", content)
        os.remove("Square.json")

    def test_save_to_file_type(self):
        '''
            Testing saving a file into json format and testing the type
        '''
        try:
            os.remove("Square.json")
        except:
            pass
        r1 = Square(5, 0, 0, 346)
        Square.save_to_file([r1])

        with open("Square.json", "r") as file:
            content = file.read()

        self.assertEqual(str, type(content))
        try:
            os.remove("Square.json")
        except:
            pass

if __name__ == "__main__":
    unittest.main()
