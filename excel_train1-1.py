#oneday study

import numpy as np
text = np.loadtxt(
	fname = "C:\App\Script\oneday\data01-train.csv",
	delimiter = ","
)

print('[Type of Data]', type(text))
print('First Two Rows')
print(text[0:1,])

print('First Two Row and Two Columns')
print(text[0:2,[0,1]])
'''
print('1000~1020')
print(text[999:1019,[9,11,2]])
'''
