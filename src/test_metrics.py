import unittest
from csv_parser import CSVParser
from metrics import get_annual_returns, YEAR, MONTH, QUARTER, DAY

test_cases = [
    ("Date,Open,High,Low,Close,Adj Close,Volume\n" +
     "2023-11-01,10,10,10,10,11,1000\n" +
     "2024-10-31,11,11,11,11,12,1200", {
         "Test": 0.10
     }, YEAR),
     ("Date,Open,High,Low,Close,Adj Close,Volume\n" +
     "2023-11-01,10,10,10,10,10,1000\n" +
     "2023-12-01,10.2,10.2,10.2,10.2,10.2,1200\n" +
     "2024-01-01,10.5,10.5,10.5,10.5,10.5,2000", {
         "Test": 0.2963
     }, MONTH
), ("Date,Open,High,Low,Close,Adj Close,Volume\n" +
     "2023-11-01,10,10,10,10,10,1000\n" +
     "2024-02-01,10.2,10.2,10.2,10.2,10.2,1200\n" +
     "2024-05-01,10.5,10.5,10.5,10.5,10.5,2000", {
         "Test": 0.0988
     }, QUARTER),
    ("Date,Open,High,Low,Close,Adj Close,Volume\n" +
     "2023-11-01,1000,1000,1000,1000,1000,10000\n" +
     "2023-11-02,1000.5,1000.5,1000.5,1000.5,1000.5,12000\n" +
     "2023-11-03,1000.3,1000.3,1000.3,1000.3,1000.3,12000", {
         "Test": 0.0547
     }, DAY)


]
class TestMetrics(unittest.TestCase):
    def test_get_annual_returns(self):
        for test_case in test_cases:
            expected_value = test_case[1]
            stock_data = CSVParser(csv_text=test_case[0]).get_clean_data()
            actual_value = get_annual_returns(stock_data)
            self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    unittest.main()