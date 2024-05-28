import os
from stock import Stock

class CSVParser:
    def __init__(self, src_directory=None, csv_text=None):
        self.__stock_data = {}
        self.__src_dir = src_directory
        self.__stock_data_clean = {}
        if self.__src_dir:
            self.__fetch()
            self.__parse_stock_data()
        else:
            self.__stock_data["Test"] = csv_text
            self.__parse_stock_data()

    def __fetch(self):
        for item in os.listdir(self.__src_dir):
            file_name = os.path.join(self.__src_dir, item)
            with open(file_name, encoding="utf-8") as csv_file:
                self.__stock_data[item.rstrip(".csv")] = csv_file.read()
    
    def get_raw_data(self):
        return self.__stock_data
    
    def get_clean_data(self):
        return self.__stock_data_clean

    def __parse_stock_data(self):
        # extract stock price data
        for stock in self.__stock_data:
            csv_string = self.__stock_data[stock]
            lines = csv_string.split("\n")
            stock_info = Stock(stock)
            heading_map = {}
            for i in range(len(lines)):
                data_points = lines[i].split(",")
                if i == 0:
                    # assume first row are column headers
                    for j in range(len(data_points)):
                        heading = data_points[j]
                        heading_map[j] = heading
                    continue
                for j in range(len(data_points)):
                    data_point = float(data_points[j]) if j != 0 else data_points[j]
                    stock_info.set_data(heading_map[j], data_point)
            self.__stock_data_clean[stock] = stock_info

