
import pandas as pd
import csv
df=pd.read_csv('C:\Users\\28708\\Desktop\\Data3-coarse.txt', header=None)
data_e=df.sample(n=15000)
print data_e
data_e.to_csv('C:\Users\\28708\\Desktop\\Data332-coarse.txt', index=None,header=0)