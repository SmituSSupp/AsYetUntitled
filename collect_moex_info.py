import pandas as pd

file_loc = "fixed_sheet.xlsx"
start_date = "2021-06-18"
end_date = "2021-08-18"


df = pd.ExcelFile(file_loc).parse('18.06.2021') #you could add index_col=0 if there's an index
moex_tickers = df[:100]['Code']
companies_and_prices = {}

for ticker in moex_tickers:
    company_prices = yf.download(ticker + '.ME', start=start_date, end=end_date, interval='1d')
    company_info = yf.Ticker(ticker + '.ME').info
    companies_and_prices[ticker] = {'prices':company_prices, 'info': company_info}