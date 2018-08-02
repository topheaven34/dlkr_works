"""
[Title] 2일차
[Program Code]
[Author] jjh
[Description] make dataframe with local file [dbms, hdfs - hadoop, spark,...]
"""

print(__doc__)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dfTrain = pd.read_csv("C:\App\Script\oneday\data01-train.csv"
	,header = None)
nObsDftrain = len(dfTrain)
print(nObsDftrain)

print(dfTrain[0:10]) #10개의 관찰지 출력
print(dfTrain.columns.values)
print(dfTrain[0:2][[1,2,12]])
# array index :
dfTrain.columns =['Y1','Y2','V1','V2','V3','V4','V5','V6','V7','V8','V9','V10','V11']


#print(dfTrain.columns.values)
#print(dfTrain[['Y1','Y2']][:10])

#plt.figure(1)
for col in dfTrain.columns:
		(kurtosis,skew)=dfTrain[col].kurtosis(),dfTrain[col].skew()
		print("{}: 첨도={}, 왜도={}".format(col,kurtosis,skew))
#dfTrain[[col]].plot.hist(stacked=True)
#plt.show()
plt.figure(1)
for col in ['V1','V2','V3','V4','V5','V6','V7','V8','V9','V10','V11']:
	dfTrain.loc[dfTrain['Y2']==0, col].plot.hist(Label="0")
	dfTrain.loc[dfTrain['Y2']==0, col].plot.hist(Label="1")
	plt.legend()
	plt.show()
#[HW]
#plt.figure(2)
#for col in ['V1','V2','V3','V4','V5','V6','V7','V8','V9','V10','V11']:
#	dfTrain.boxplot(columns=[col],by='Y2')
#	plt.show()

#import pandas as pd
#df = pd.read_csv(
#	filepath_or_buffer = "C:\App\Script\oneday\cust_data.csv"
#	, sep = ','
#	, encoding = "ISO-8859-1"
#	)
#, header = None
#print('Type of df', type(df))
#print('df.dtypes')
#print(df.dtypes)
#print(df.head(3))

#df.columns = ['NUM_OF_PATH','PAGEVIEW','SESSION','AVG_PAGEVIEW','REVENUE','TRANSACTION','AVG_PURCHARSE_PRICE','DURATION','AVG_DURATION','PUR_PRODUCT_Q','QUANTITY','LAST_PUR_DATE','GENDER','AGE','PRE_GRADE','LAST_GRADE','CITY','MOBILE_BRAND','SESSION_PUR','SESSION_NOPUR']
#print(df(count())
#print(df['NUM_OF_PATH'].count())
#print(df.groupby(df.NUM_OF_PATH).count()
#print(df.NUM_OF_PATH.groupby(df.NUM_OF_PATH).count())
#print(df.NUM_OF_PATH.where(df.REVENUE<8000).groupby(df.NUM_OF_PATH).count())


#print(df.head5)
#[HW] NUM_OF_PATH 별 (최대금액-최대바로 아래금액) / 최대바로 아래금액 계산

#import pandasql as pdsql
#pysql = lambda q: pdsql.sqldf(q, globals())

#sql = "select NUM_OF_PATH, count(*) from df group by NUM_OF_PATH"
#dfSql = pysql(sql)
#print(dfSql)
