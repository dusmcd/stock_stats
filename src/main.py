from csv_parser import CSVParser
from metrics import get_time_periods


def main():
    parser = CSVParser("./inputs")
    stock_data = parser.get_clean_data()
    get_time_periods(stock_data["LUV"])


if __name__ == "__main__":
    main()