import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

# define date range
start=dt.datetime(2018,1,1)
end=dt.datetime(2018,12,31)

# get data for defined date range
df=web.DataReader('TSLA','yahoo',start,end)

# CSV export and import
df.to_csv('tesla.csv')
df = pd.read_csv('tesla.csv', parse_dates=True, index_col=0)

# 100 Moving Average
df['100ma'] = df['Adj Close'].rolling(window=100).mean()
df.dropna(inplace=True)

# print first 10 records
print(df.head(10))

# plot graph

#df.plot()

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (0,0), rowspan=1, colspan=1, sharex=ax1)

ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.plot(df.index, df['Volume'])

plt.show
