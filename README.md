This tool parses CSV files containing stock price information and displays the
corresponding ticker symbols and annualized returns.

# Instructions

1. In the roof of the project create an ```inputs``` directory
2. In this newly-created directory, place as many CSV files as you want (see **File Format** section below)
3. In the root directory, execute the following command: ```./main.sh``` (You may need to add executable executable permissions with ```chmod +x```)

## File Format

The required format follows the format used in [Yahoo Finance](https://finance.yahoo.com/quote/MSFT/history).
The following columns (date type) are required:
- Date (date)
- Open (number)
- High (number)
- Low (number)
- Close (number)
- Adj Close (number)
- Volume (number)