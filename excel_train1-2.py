#oneday study 2th


import pandas as pd
df = pd.read_csv(
	filepath_or_buffer = "C:\App\Script\oneday\data01-train.csv"
	, sep = ','
	, header = None
	)
print('Type of df', type(df))
print('df.dtypes')
print(df.dtypes)
print(df.head(3))
