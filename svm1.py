# - * - coding:utf - 8 -*-
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
import random
import time
import copy
import Get_Params
# from scipy.stats.vonmises_cython import numpy
from numpy import select
import csv
import os
curr_time1=time.time()
def Get_newdata(file_id, true_node_num, ratio):
    fp = open("C:\Users\\28708\\Desktop\\Data3335-DataSyn.csv", "r")
    # fp = open("C:\Users\\28708\\Desktop\\4.txt", "r")
    multilist = [[] for row in range(true_node_num)]
    i = 0
    while 1:
        line = fp.readline()
        if not line:
            break
        pass  # do something
        line = line.strip("\n")
        temp = line.split(",")
        att_num = len(temp)
        # print att_num
        # print(i)
        for eachit in temp:
            multilist[i].append(eachit)

        i = i + 1
    node_num = i
    # print node_num
    n = int(ratio * node_num)
    samplelist = []
    sample_order = random.sample(range(node_num), n)
    for i in sample_order:
        samplelist.append(multilist[i])
    return samplelist, n, att_num


def Get_traindata2(datalist, column):
    newdata = map(list, zip(*datalist))
    x = []
    y = newdata[column]
    for i in range(len(newdata)):
        if i != column:
            x.append(newdata[i])
    x = map(list, zip(*x))
    return x, y


def Data_construct(data_list, column_num, ratio):
    node_num = len(data_list)
    n = int(ratio * node_num)
    random.seed(1)
    sample_order = random.sample(range(node_num), n)
    train_data = []
    test_data = []
    for i in range(node_num):
        if i in sample_order:
            train_data.append(data_list[i])
        else:
            test_data.append(data_list[i])

    train_x, train_y = Get_traindata2(train_data, column_num)
    single_error = (len(set(train_y)) == 2)
    test_x, test_y = Get_traindata2(test_data, column_num)

    return train_x, train_y, test_x, test_y, single_error

# """
def SVM_evaluation(train_x, train_y, test_x, test_y):
    if len(set(train_y)) < 2:
        svm_y = [train_y[0] for i in range(len(test_x))]
    else:
        clf = svm.SVC()
        clf.fit(train_x, train_y)

        svm_y = clf.predict(test_x)
        svm_y = svm_y.tolist()

    right_num = 0.0
    for i in range(len(test_y)):
        if svm_y[i] == test_y[i]:
            right_num += 1.0
    right_ratio = right_num / len(test_y)
    return right_ratio
# """

def RF_evaluation(train_x, train_y, test_x, test_y):
    clf = RandomForestClassifier()
    clf.fit(train_x, train_y)
    right_ratio = clf.score(test_x, test_y)
    return right_ratio


def SVM_ratio(train_x, train_y, test_x, test_y, loop_time, classifier):
    rightratio = 0.0
    for i in range(loop_time):
        # print('now processing loop:')
        if i % 5 == 0:
            print(i),
        if classifier == 'SVM':
            right_ratio = SVM_evaluation(train_x, train_y, test_x, test_y)
        else:
            right_ratio = RF_evaluation(train_x, train_y, test_x, test_y)
        rightratio += right_ratio
    meanratio = rightratio / (1.0 * loop_time)
    return meanratio
# """
att_num,node_num,true_node_num,rowlist,multilist=Get_Params.get_file_info(3,50000,0.01)
print ("att_num",att_num)

#
multilist2,node_num2,att_num2=Get_newdata(20,true_node_num, 0.01)
print ("true_node_num",true_node_num)
#
#
print(node_num2,att_num2)
# print(multilist)
# print(multilist2)
loop_time=10
col=1
m1=0.0
m2=0.0
leng=0
col_list=range(att_num)
for col in col_list:
    ratio = 0.7
    loop_time = 1
    # col=1
    leng = len(col_list)
    col_all = range(att_num)
    train_x,train_y,test_x,test_y,single_err=Data_construct(multilist, col, ratio)
    train_x2,train_y2,test_x2,test_y2,single_err2=Data_construct(multilist2, col, ratio)
    if ((not single_err)):
        print(col,'omit!')
        continue
    else:
        leng=leng+1
        t1=SVM_ratio(train_x, train_y, test_x, test_y, loop_time,'SVM')
        m1=m1+t1
        if (not single_err2):
            t2=0.5
        else:
            t2=SVM_ratio(train_x2, train_y2, test_x, test_y, loop_time,'SVM')
        m2=m2+t2
        print('col:',col,' ',t1,t2)

print ("m1",m1)
print ("m2",m2)
print leng
curr_time2=time.time()
total_time=curr_time2-curr_time1
print total_time
write_list1 = [[m1/5,m2/5,total_time]]
print(write_list1)
os.chdir('C:\Users\\28708\\Desktop\\57\\output')
with open('file-' + str(390) + '1-SVM_syn_datatime_R.csv', 'a') as fid:
        fid_csv = csv.writer(fid)
        fid_csv.writerows(write_list1)






