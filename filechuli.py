import numpy as np
import pandas as pd
import csv
########Retail set
"""
########delete e and g 
df = pd.read_csv('C:\Users\\28708\\Desktop\\4.txt', header=None)
df.drop([df.columns[4]], axis=1,inplace=True)
df.drop([df.columns[5]], axis=1,inplace=True)
# x = np.delete(df,[5,7],axis=1)
print df
df.to_csv('C:\Users\\28708\\Desktop\\5.txt',index = None)
# np.savetxt(df, 'C:\Users\\28708\\Desktop\\aa.txt')
# with open('C:\Users\\28708\\Desktop\\5.txt', 'r') as f:
#     print(df.read())
# """
"""
input_domain='C:\Users\\28708\\Desktop\\python_highdim\\data\\Data5-coarse.domain'
fd=open(input_domain,'r')
head_line=fd.readline()
readrow=head_line.split(" ")
print(readrow)
"""
"""
list1 = []
# filename='C:\Users\\28708\\Desktop\\4.txt'
try:
	file = open('C:\Users\\28708\\Desktop\\4.txt', 'r')
except IOError:
	print "Sorry,the file does't exist."
else:
    lines = file.readlines()
    for line in lines:
        a = line.split(',')
        x = a[4]
        list1.append(x)
file.close()

for x in list1:
    print(x)
# df.to_csv('C:\Users\\28708\\Desktop\\6.txt',index = None)
"""
"""
data = pd.read_csv('C:\Users\\28708\\Desktop\\4.txt', header=None)
data_e = data.iloc[:, 4]
data_g=data.iloc[:, 6]
# print data_e,data_g
data_e.to_csv('C:\Users\\28708\\Desktop\\6.txt',index = None)
data_g.to_csv('C:\Users\\28708\\Desktop\\7.txt',index = None)
"""
import numpy as np
import pandas as pd
import csv
########Adult set
# data = pd.read_csv('C:\Users\\28708\\Desktop\\Data2-coarse.txt', header=None)
# print data
#########Adult set
"""
col_n=[0,2,5,7,9,11,12,14]
data_e=pd.DataFrame(data,columns=col_n)
print data_e
data_e.to_csv('C:\Users\\28708\\Desktop\\Data20-coarse.txt', index=None,header=0)
"""
"""
col_n=[8,13]
data_e=pd.DataFrame(data,columns=col_n)
print data_e
data_e.to_csv('C:\Users\\28708\\Desktop\\Data21-coarse.txt', index=None,header=0)
"""
"""
col_n=[3,4,6]
data_e=pd.DataFrame(data,columns=col_n)
print data_e
data_e.to_csv('C:\Users\\28708\\Desktop\\Data22-coarse.txt', index=None,header=0)
"""
"""
col_n=[1,10]
data_e=pd.DataFrame(data,columns=col_n)
print data_e
data_e.to_csv('C:\Users\\28708\\Desktop\\Data23-coarse.txt', index=None,header=0)
"""
#######TPC-E set
data_tcpe = pd.read_csv('C:\Users\\28708\\Desktop\\Data333-coarse.txt', header=None)
# print data_tcpe
"""
col_n=[0,1,2,4,5,6,7,9,12,13,14,15,16,17,18,19,20,21,22]
data_e=pd.DataFrame(data_tcpe,columns=col_n)
print data_e
data_e.to_csv('C:\Users\\28708\\Desktop\\Data3331-coarse.txt', index=None,header=0)
"""
# col_n=[3]
# data_e=pd.DataFrame(data_tcpe,columns=col_n)
# print data_e
# data_e.to_csv('C:\Users\\28708\\Desktop\\Data3332-coarse.txt', index=None,header=0)
col_n=[23]
data_e=pd.DataFrame(data_tcpe,columns=col_n)
print data_e
data_e.to_csv('C:\Users\\28708\\Desktop\\Data3336-coarse.txt', index=None,header=0)

