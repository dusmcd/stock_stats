class Stock:
    def __init__(self, ticker):
        self.__information = {
            "Date": [],
            "Open": [],
            "High": [],
            "Low": [],
            "Close": [],
            "Adj Close": [],
            "Volume": []
        }
        self.ticker = ticker

    def set_data(self, heading, data_point):
        self.__information[heading].append(data_point)

    def rate_of_return(self, periods):
        pv = self.__information["Close"][0]
        fv = self.__information["Close"][-1]
        return ((fv/ pv) ** (1 / periods)) - 1
    
    def get_number_of_periods(self):
        return len(self.__information["Date"]) - 1

    def __repr__(self):
        return str(self.__information)

    