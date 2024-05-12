import pandas as pd  
import matplotlib.pyplot as plt  
import yfinance as yf 

msft = yf.Ticker('msft')
stockinfo =msft.info

#for key,value in stockinfo.items():
    #print(key,":",value)
#print(type(msft.institutional_holders))
#print(type(msft.splits))

df1= msft.institutional_holders
df2= msft.splits
df3=msft.dividends
print(df1,df2,df3)

df=yf.download('msft','2023-01-01','2024-01-01')
print(df.head())
plt.plot(df.index,df['Close'])
plt.show()


