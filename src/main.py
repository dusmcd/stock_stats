from csv_parser import CSVParser


def main():
    parser = CSVParser("./inputs")
    stock_data = parser.get_clean_data()
    print(stock_data)


if __name__ == "__main__":
    main()