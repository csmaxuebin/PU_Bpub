import Get_Params
import Get_Rappor
import numpy
import itertools
import random
import time
import os
import csv
import pandas as pd
import re

from scipy import *
import numpy as np
import scipy.stats
from JunctionTree import independent_marginal2, independent_marginal, independent_marginal3
from Estimate_Joint_Distribution import true_joint_distribution, unfold_pro_list
from numpy import power


def get_clique(range_size, clique_size, sample_size):
    ini_list2 = list(itertools.combinations(range(range_size), clique_size))
    zzz = [list(eachtuple) for eachtuple in ini_list2]
    random.seed(15)
    zlist = random.sample(zzz, sample_size)
    return zlist


def l2_err(pro, true_pro):
    leng = len(pro)
    delta_pro = numpy.array(pro) - numpy.array(true_pro)
    return 1.0 * numpy.sqrt(numpy.sum(numpy.power(delta_pro, 2)) / (1.0))


def get_avd(pro, true_pro):
    leng = len(pro)
    delta_pro = numpy.array(pro) - numpy.array(true_pro)
    #     max_delta=max(numpy.abs(delta_pro))
    #     return max_delta
    return (sum(list(abs(delta_pro)))/2.0)
    # abs_delta = numpy.abs(delta_pro)
    # return numpy.sum(abs_delta) / 2.0


def cos(vector1, vector2):
    dot_product = 0.0;
    normA = 0.0;
    normB = 0.0;
    for a, b in zip(vector1, vector2):
        dot_product += a * b
        normA += a ** 2
        normB += b ** 2
    if normA == 0.0 or normB == 0.0:
        return None
    else:
        return dot_product / ((normA * normB) ** 0.5)


def get_max(pro, true_pro):
    max1 = max(pro)
    max2 = max(true_pro)

    return abs(max1 - max2)


def get_var(pro, true_pro):
    return numpy.var(numpy.array(pro) - numpy.array(true_pro))
"""
def asymmetricKL(pro,true_pro):
    k_x = set(pro)
    p = []
    for i in k_x:
        p.append(pro.count(i) / len(pro))

    k_y = set(true_pro)
    q = []
    for i in k_y:
        q.append(true_pro.count(i) / len(true_pro))

    KL = 0.0
    for i in range(len(k_x)):
        KL += p[i] * log(p[i] / q[i], 2)
    return (round(KL, 2))
"""



    # return sum(pro * log(pro / true_pro))




fai_C = 0.4  # from 0.2, 0.3, 0.4, 0.5
f = 0.5  # from 0.1, 0.2, 0.3, 0.4, 0.5  *********
bloombit = 32
hashbit = 16
dt = 0.01
readlimit = 60000
samplerate = 0.01
sparse_rate = 0.0
data = pd.read_csv('C:\Users\\28708\\Desktop\\DisHD\\out\\file-4100true_pro_marginal40.csv', header=None)
# print data.iloc[1][2]
avd_list=[]
avd_list1=[]
var_list=[]
var_list1=[]
js_list=[]
js_list1=[]
# l2_errlist=[]
# l2_errlist1=[]
# """
for i in range(0,20):
   dyn_string=data.iloc[i][5]
   dyn_numbers=re.findall(r"\d+\.?\d*",dyn_string)
   dyn_number = [ float(x) for x in dyn_numbers ]
   print (i,dyn_number)
   dyn_string1 = data.iloc[i][2]
   dyn_numbers1 = re.findall(r"\d+\.?\d*", dyn_string1)
   dyn_number1 = [float(x) for x in dyn_numbers1]
   print (i, dyn_number1)
   true_string=data.iloc[i][0]
   true_numbers=re.findall(r"\d+\.?\d*",true_string)
   true_number = [float(x) for x in true_numbers ]

   print (i,true_number)
   # a=np.array(dyn_number)
   # c=np.array(dyn_number1)
   # b=np.array(true_number)
   # print ("aaa:",a-b)
   # print ("bbba", c - b)
   print (i,get_avd(dyn_number,true_number))
   print (i, get_avd(dyn_number1, true_number))
   # print (i, asymmetricKL(dyn_number, true_number))
   # print (i, asymmetricKL(dyn_number1, true_number))
   # print (i, l2_err(dyn_number, true_number))
   # print (i, l2_err(dyn_number1, true_number))
   # var_list.append(get_var(dyn_number, true_number))
   # var_list1.append(get_var(dyn_number1, true_number))
   # js_list.append(asymmetricKL(dyn_number, true_number))
   # js_list1.append(asymmetricKL(dyn_number1, true_number))
   avd_list.append(get_avd(dyn_number,true_number))
   avd_list1.append(get_avd(dyn_number1, true_number))
   # l2_errlist.append(l2_err(dyn_number, true_number))
   # l2_errlist1.append(l2_err(dyn_number1, true_number))
print avd_list
print avd_list1
# print var_list
# print var_list1
# print js_list
# print js_list1
# print sum(var_list)/20
# print sum(var_list1)/20
print sum(avd_list)/20
print sum(avd_list1)/20
# print sum(l2_errlist)/20
# print sum(l2_errlist1)/20
# """
write_list1 = [[0.1, avd_list[0],avd_list1[0],sum(avd_list)/20, sum(avd_list1)/20]]
# write_list2 = [[0.5,sum(var_list)/20, sum(var_list1)/20]]
print(write_list1)
os.chdir('C:\Users\\28708\\Desktop\\DisHD\\outp')
with open('file-' + str(40) + 'pro_marginal100.csv', 'a') as fid:
    fid_csv = csv.writer(fid)
    fid_csv.writerows(write_list1)
    # fid_csv.writerows(write_list2)
