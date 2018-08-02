"""
[Title] 2일차
[Program Code]
[Author] jjh
[Description] make dataframe with local file [dbms, hdfs - hadoop, spark,...]
"""
import pandas as pd
df = pd.read_csv(
	filepath_or_buffer = "C:\App\Script\oneday\cust_data.csv"
	, sep = ','
	, encoding = "ISO-8859-1"
	)
#, header = None
#print('Type of df', type(df))
#print('df.dtypes')
#print(df.dtypes)
#print(df.head(3))

df.columns = ['NUM_OF_PATH','PAGEVIEW','SESSION','AVG_PAGEVIEW','REVENUE','TRANSACTION','AVG_PURCHARSE_PRICE','DURATION','AVG_DURATION','PUR_PRODUCT_Q','QUANTITY','LAST_PUR_DATE','GENDER','AGE','PRE_GRADE','LAST_GRADE','CITY','MOBILE_BRAND','SESSION_PUR','SESSION_NOPUR']
#print(df(count())
#print(df['NUM_OF_PATH'].count())
#print(df.groupby(df.NUM_OF_PATH).count()
#print(df.NUM_OF_PATH.groupby(df.NUM_OF_PATH).count())
print(df.NUM_OF_PATH.where(df.REVENUE<8000).groupby(df.NUM_OF_PATH).count())


#print(df.head5)
#NUM_OF_PATH 별 (최대금액-최대바로 아래금액) / 최대바로 아래금액 계산

#import pandasql as pdsql
#pysql = lambda q: pdsql.sqldf(q, globals())

#sql = "select NUM_OF_PATH, count(*) from df group by NUM_OF_PATH"
#dfSql = pysql(sql)
#print(dfSql)
