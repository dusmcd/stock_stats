class Stock:
    def __init__(self, ticker):
        self.__dates = []
        self.__opens = []
        self.__highs = []
        self.__lows = []
        self.__closes = []
        self.__adj_closes = []
        self.__volumes = [] 
        self.__heading_map = {
            "Date": self.__dates,
            "Open": self.__opens,
            "High": self.__highs,
            "Low": self.__lows,
            "Close": self.__closes,
            "Adj Close": self.__adj_closes,
            "Volume": self.__volumes
        }
        self.ticker = ticker

    def set_data(self, heading, data_point):
        self.__heading_map[heading].append(data_point)

    def rate_of_return(self, pv, fv, periods):
        return ((fv/ pv) ** (1 / periods)) - 1

    def __repr__(self):
        return str(self.__heading_map)

    