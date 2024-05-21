class Financials:
    def __init__(self, reporting_period, key_line_items):
        self.reporting_period = reporting_period
        # a dictionary of key line items (e.g., net income, current assets, etc.)
        self.key_line_items = key_line_items

    def price_earnings_ratio(self, eps, price, shares_outstanding):
        price_per_share = price / shares_outstanding
        return price_per_share / eps

    def return_on_equity(self, net_income, total_equity):
        pass

    def return_on_assets(self, net_income, total_assets):
        pass

    def current_ratio(self, current_assets, current_liabilities):
        pass

    def days_sales_inventory(self, cogs, beg_invenventory, end_inventory):
        pass

    def days_sales_ar(self, net_sales, beg_ar, end_ar):
        pass

    def free_cash_flow(self, operating_cash, **args):
        pass