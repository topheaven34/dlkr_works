#2day test

import pandas as pd
col_names=['Y1','Y2','X1','X2','X3','X4','X5','X6','X7','X8','X9','X10']
dfTrain = pd.read_csv("C:\App\Script\oneday\data01-train.csv",names=col_names)
dfSummary = dfTrain.describe()
dfSummary.to_csv("C:\App\Script\oneday\data01-train-output2.csv",header=col_names)
arrTrain=dfTrain.as_matrix().astype(int)
