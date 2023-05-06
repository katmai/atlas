import unittest
from improved_river_code import river_flow

class TestRiverFlow(unittest.TestCase):
    def test_river_flow(self):
        expected_output = ['The river flows', 'The water rushes by', 'The river flows']
        self.assertEqual(river_flow(), expected_output)

if __name__ == '__main__':
    unittest.main()