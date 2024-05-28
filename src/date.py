class Date:
    def __init__(self, date_string):
        # expecting format yyyy-mm-dd
        self.year = int(date_string[0:4])
        self.month = int(date_string[5:7])
        self.day = int(date_string[8:])
        # ignoring leap year for now
        self.__last_days = {
            "1": 31,
            "2": 28,
            "3": 31,
            "4": 30,
            "5": 31,
            "6": 30,
            "7": 31,
            "8": 31,
            "9": 30,
            "10": 31,
            "11": 30,
            "12": 31
        } 
        self.__date_string = date_string

    def get_next_day(self):
        day = self.day + 1
        year = self.year
        month = self.month
        if self.day == self.__last_days[str(self.month)] and self.month == 12:
            year += 1
            month = 1
            day = 1
        elif self.day == self.__last_days[str(self.month)]:
            day = 1
            month += 1
        self.__date_string = f"{year}"
        if month < 10:
            self.__date_string += f"-0{month}"
        else:
            self.__date_string += f"-{month}"
        if day < 10:
            self.__date_string += f"-0{day}"
        else:
            self.__date_string += f"-{day}"
        
        return Date(self.__date_string)

    def __add__(self, number):
        current_date = self
        for i in range(number):
            current_date = current_date.get_next_day()
        return current_date

    def __sub__(self, other):
        raise NotImplementedError
    
    def __repr__(self):
        return self.__date_string