import pandas_datareader.data as web

start = '2016-01-01'
end = '2020-12-31'

df = web.get_data_yahoo('F', start=start, end=end)

print(df.head())
