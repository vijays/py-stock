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

# print first 10 records
print(df.head(10))
