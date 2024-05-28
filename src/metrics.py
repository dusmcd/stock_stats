
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

def get_annual_returns(stock_data, reporting_period):
    annual_returns = {}
    for stock in stock_data:
        periods = stock_data[stock].get_number_of_periods()
        raw_rate = stock_data[stock].rate_of_return(periods)
        annual_return = round(raw_rate * multiplier_map[reporting_period], 4)
        annual_returns[stock] = annual_return
    return annual_returns

def get_time_periods(stock):
    dates = stock.get_dates()