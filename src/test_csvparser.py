import unittest
from csv_parser import CSVParser
from stock import Stock

test_cases = [
    ("Date,Open,High,Low,Close,Adj Close,Volume\n" +
     "2024-05-20, 23.4, 34, 54, 52, 12, 45450",
      str({
          "Date": ["2024-05-20"],
          "Open": [23.4],
          "High": [34.0],
          "Low": [54.0],
          "Close": [52.0],
          "Adj Close": [12.0],
          "Volume": [45450.0]
      })),
      ("Date,Open,High,Low,Close,Adj Close,Volume\n" +
       "2024-06-21, 21, 21, 21, 21, 21, 2000\n" +
       "2024-06-22, 22, 22, 22, 22, 22, 3000",
       str({
           "Date": ["2024-06-21", "2024-06-22"],
           "Open": [21.0, 22.0],
           "High": [21.0, 22.0],
           "Low": [21.0, 22.0],
           "Close": [21.0, 22.0],
           "Adj Close": [21.0, 22.0],
           "Volume": [2000.0, 3000.0]
       }))
]
class TestCSVParser(unittest.TestCase):
    def test_parser(self):
        for test_case in test_cases:
            expected_value = test_case[1]
            parser = CSVParser(csv_text=test_case[0])
            stock = str(parser.get_clean_data()["Test"])
            self.assertEqual(expected_value, stock)


if __name__ == "__main__":
    unittest.main()