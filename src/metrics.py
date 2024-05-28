from date import Date

QUARTER = "quarters"
DAY = "days"
YEAR = "years"
MONTH = "months"

multiplier_map = {
    QUARTER: 4,
    DAY: 365,
    YEAR: 1,
    MONTH: 12
}

def get_annual_returns(stock_data):
    annual_returns = {}
    for stock in stock_data:
        periods = stock_data[stock].get_number_of_periods()
        if periods < 1:
            raise Exception("You need more at least two dates to calculate returns")
        raw_rate = stock_data[stock].rate_of_return(periods)
        reporting_period = get_time_periods(stock_data[stock])
        annual_return = round(raw_rate * multiplier_map[reporting_period], 4)
        annual_returns[stock] = annual_return
    return annual_returns

def get_time_periods(stock):
    dates = stock.get_dates()
    date1 = Date(dates[0])
    date2 = Date(dates[1])
    if date1.get_next_day() == date2:
        return DAY
    if date1.subtract_months(date2) == 1:
        return MONTH
    if date1.subtract_months(date2) == 3:
        return QUARTER
    if date2.year - date1.year == 1:
        return YEAR
    raise Exception("Not a valid time period")