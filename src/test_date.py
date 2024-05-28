import unittest
from date import Date

test_cases_init = [
    ("2023-05-01", (2023, 5, 1)),
    ("2024-07-13", (2024, 7, 13)),
    ("2024-10-31", (2024, 10, 31))
]
test_cases_next = [
    ("2023-05-01", (2023, 5, 2)),
    ("2024-05-31", (2024, 6, 1)),
    ("2024-11-30", (2024, 12, 1)),
    ("2024-02-28", (2024, 3, 1)),
    ("2023-12-31", (2024, 1, 1))
]
test_cases_eq = [
    "2023-05-01",
    "2024-05-31",
    "2024-11-30",
    "2024-02-28",
    "2023-12-31"
]
class TestDate(unittest.TestCase):
    def test_init(self):
        for test_case in test_cases_init:
            expected = test_case[1]
            actual = Date(test_case[0])
            self.assertEqual(expected[0], actual.year)
            self.assertEqual(expected[1], actual.month)
            self.assertEqual(expected[2], actual.day)
    
    def test_next_day(self):
        for test_case in test_cases_next:
            expected = test_case[1]
            actual = Date(test_case[0]).get_next_day()
            self.assertEqual(expected[0], actual.year)
            self.assertEqual(expected[1], actual.month)
            self.assertEqual(expected[2], actual.day)

    def test_eq(self):
        for test_case in test_cases_eq:
            date1 = Date(test_case)
            date2 = Date(test_case)
            self.assertTrue(date1 == date2)

if __name__ == "__main__":
    unittest.main()