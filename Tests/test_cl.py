import unittest
from ProductionCode.basic_cl import *

class TestWeatherData(unittest.TestCase):
    def test_load_valid_file(self):
        """Tests whether data from a valid CSV file is loaded successfully."""
        load_data()
        self.assertGreater(len(data), 0)

if __name__ == '__main__':
    unittest.main()