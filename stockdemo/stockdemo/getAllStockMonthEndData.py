# read cvs file under data/IBB.csv

#loop every ticker
df = pd.read_csv('data/IBB_holdings_sorted.csv',low_memory=False, delimiter=',', header=0, encoding='ascii')
ticker_list=df["Ticker"].tolist()
print(ticker_list)

for t in ticker_list:


#result = getTickerMonthEndDataList('ARRY')
#print(result)

#merge list

#save to new csv
