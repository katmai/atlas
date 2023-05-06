import unittest


class TestAddNumbers(unittest.TestCase):
    def test_add_numbers_with_integers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)

    def test_add_numbers_with_non_integers(self):
        with self.assertRaises(TypeError):
            add_numbers(2.5, "3")

if __name__ == '__main__':
    unittest.main()