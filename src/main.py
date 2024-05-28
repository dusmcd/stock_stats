from csv_parser import CSVParser
from metrics import get_annual_returns


def main():
    try:
        parser = CSVParser("./inputs")
        stock_data = parser.get_clean_data()
        show_stock_returns(stock_data)
    except Exception as e:
        print("SOMETHING WENT WRONG. HERE IS THE ERROR:")
        print(e)

def show_stock_returns(stock_data):
    annual_returns = get_annual_returns(stock_data)
    print("TICKER\t\tANNUALIZED RETURN")
    print("======\t\t=================")
    for ticker in annual_returns:
        print(f"{ticker}\t\t{annual_returns[ticker] * 100}%")


if __name__ == "__main__":
    main()