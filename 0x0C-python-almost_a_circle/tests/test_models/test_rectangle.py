import unittest
from io import StringIO
import sys
from models.rectangle import Rectangle

class Test_rectangle(unittest.TestCase):
    def test_class(self):
        rectangle = Rectangle(10, 2, 4, 5)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.x, 4)
        self.assertEqual(rectangle.y, 5)
        self.assertEqual(rectangle.id, 2)

        rectangle = Rectangle(10, 2, 0, 0)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)
        self.assertEqual(rectangle.id, 3)
        rectangle = Rectangle(10, 2, 4, 5, 10)
        self.assertEqual(rectangle.id, 10)

    def test_getter_width(self):
        rectangle = Rectangle(10, 2, 4, 5)
        self.assertEqual(rectangle.width, 10)
    
    def test_setter_width(self):
        rectangle = Rectangle(10, 2, 4, 5)
        rectangle.width = 12
        self.assertEqual(rectangle.width, 12)

        with self.assertRaises(TypeError) as error1:
            rectangle = Rectangle('2', 4)
        self.assertEqual(str(error1.exception), "width must be an integer")
        
        with self.assertRaises(TypeError) as error2:
            rectangle = Rectangle(1.5, 4)
        self.assertEqual(str(error2.exception), "width must be an integer")
        
        with self.assertRaises(ValueError) as error3:
            rectangle = Rectangle(-7, 4)
        self.assertEqual(str(error3.exception), "width must be > 0")

    def test_getter_height(self):
        rectangle = Rectangle(10, 2, 4, 5)
        self.assertEqual(rectangle.height, 2)
    
    def test_setter_height(self):
        rectangle = Rectangle(10, 2, 4, 5)
        rectangle.height = 7
        self.assertEqual(rectangle.height, 7)

        with self.assertRaises(TypeError) as error1:
            rectangle = Rectangle(2, '4')
        self.assertEqual(str(error1.exception), "height must be an integer")
        
        with self.assertRaises(TypeError) as error2:
            rectangle = Rectangle(2, 4.2)
        self.assertEqual(str(error2.exception), "height must be an integer")
        
        with self.assertRaises(ValueError) as error3:
            rectangle = Rectangle(3, -4)
        self.assertEqual(str(error3.exception), "height must be > 0")

    def test_getter_x(self):
        rectangle = Rectangle(10, 2, 4, 5)
        self.assertEqual(rectangle.x, 4)
    
    def test_setter_x(self):
        rectangle = Rectangle(10, 2, 4, 5)
        rectangle.x = 9
        self.assertEqual(rectangle.x, 9)

        with self.assertRaises(TypeError) as error1:
            rectangle = Rectangle(2, 4, '7', 8)
        self.assertEqual(str(error1.exception), "x must be an integer")
        
        with self.assertRaises(TypeError) as error2:
            rectangle = Rectangle(2, 4, 2.3, 4)
        self.assertEqual(str(error2.exception), "x must be an integer")
        
        with self.assertRaises(ValueError) as error3:
            rectangle = Rectangle(3, 4, -3, 2)
        self.assertEqual(str(error3.exception), "x must be >= 0")
    
    def test_getter_y(self):
        rectangle = Rectangle(10, 2, 4, 5)
        self.assertEqual(rectangle.y, 5)
    
    def test_setter_y(self):
        rectangle = Rectangle(10, 2, 4, 5)
        rectangle.y = 10
        self.assertEqual(rectangle.y, 10)

        with self.assertRaises(TypeError) as error1:
            rectangle = Rectangle(2, 4, 7, '8')
        self.assertEqual(str(error1.exception), "y must be an integer")
        
        with self.assertRaises(TypeError) as error2:
            rectangle = Rectangle(2, 4, 2, 4.5)
        self.assertEqual(str(error2.exception), "y must be an integer")
        
        with self.assertRaises(ValueError) as error3:
            rectangle = Rectangle(3, 4, 3, -2)
        self.assertEqual(str(error3.exception), "y must be >= 0")

    def test_area(self):
        rectangle = Rectangle(4, 5)
        self.assertEqual(rectangle.area(), 20)
    
    def test_display(self):
        # Redirect stdout
        captured_output = StringIO()
        sys.stdout = captured_output

        # Create a Rectangle object
        rectangle = Rectangle(3, 2, 1, 2)
        rectangle.display()

        # Get the printed output
        printed_output = captured_output.getvalue()
        # Restore stdout
        sys.stdout = sys.__stdout__
        # Compare the printed output with the expected output
        self.assertEqual(printed_output, "\n\n ###\n ###\n")

    def test_str_(self):
        rectangle = Rectangle(2, 4, 8, 5, 10)
        self.assertEqual(str(rectangle), '[Rectangle] (10) 8/5 - 2/4')
        rectangle = Rectangle(2, 4, 8, 5)
        self.assertEqual(str(rectangle), '[Rectangle] ({}) 8/5 - 2/4'.format(rectangle.id))
