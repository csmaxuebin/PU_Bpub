import pandas as pd
import csv
"""
df=pd.read_csv('C:\Users\\28708\\Desktop\\Data333-coarse.txt', header=None)
data_e=df.sample(n=150)
print data_e
data_e.to_csv('C:\Users\\28708\\Desktop\\Data_simpal332-coarse.txt', index=None,header=0)
"""
df=pd.read_csv('C:\Users\\28708\\Desktop\\37\\3305-DataSyn.csv', header=None)
data_e=df.sample(n=1500)
print data_e
data_e.to_csv('C:\Users\\28708\\Desktop\\Data3305-DataSyn.csv', index=None,header=0)