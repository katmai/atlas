# Import necessary libraries
import unittest
from river_simulation import River

class TestRiver(unittest.TestCase):
    def setUp(self):
        self.river = River()
        
    def test_flow(self):
        self.river.flow()
        
if __name__ == '__main__':
    unittest.main()