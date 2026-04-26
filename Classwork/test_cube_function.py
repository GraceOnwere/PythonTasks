import unittest
import cube

class TestCubeFunction(unittest.TestCase):
    def test_that_cube_function_exists(self):
        cube.cube(3)

    def test_that_cube_function_return_correct_result(self):
        actual = cube.cube(3)
        expected = 27
        self.assertEqual(actual,expected)
        actual = cube.cube(3)
        expected = 27
        self.assertEqual(actual,expected)
        actual = cube.cube(5)
        expected = 125
        self.assertEqual(actual,expected)
    
    def test_that_cube(self):
        actual = cube.cube("musa")
        expected = "invalid input"
        self.assertEqual(actual,expected)
