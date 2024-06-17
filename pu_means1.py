
from sklearn.cluster import SpectralClustering
from sklearn import metrics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
Scores = [0]
Scores1 = [0]
"""
######Adult set
A = np.array([[0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
                  [0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                  [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                  [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                  [1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
                  [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0]])
"""
# """
######Retail set
A = np.array([[0 ,1 ,1, 1, 1, 1, 1 ,1 ,1 ,1 ,1, 1, 1 ,1, 1, 1],
              [1, 0, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1, 1],
              [1 ,1 ,0 ,1 ,1, 1, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1, 1],
              [1, 1, 1, 0, 0, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1],
              [1 ,1 ,1, 0, 0, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1],
              [1 ,1, 1, 1, 1, 0, 1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1],
              [1, 1, 1, 1, 1, 1, 0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1],
              [1, 1, 1, 1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1],
              [1, 1, 1, 1, 1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1],
              [1, 1, 1, 1 ,1 ,1 ,1, 1 ,1 ,0 ,1 ,1 ,1, 1, 1 ,1],
              [1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1],
              [1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1],
              [1, 1, 1, 1, 1 ,1, 1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1],
              [1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1, 1, 0 ,1 ,1],
              [1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1],
              [1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1, 1, 1 ,1 ,1 ,1 ,1 ,0]])
              # """
######TPC-E set
"""
A = np.array(
[[0 ,1, 1, 1, 1, 1, 1, 1 ,0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
 [1 ,0 ,0 ,0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
 [1 ,1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1, 1 ,1, 1],
 [1 ,1 ,1 ,1 ,1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [0 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 0, 0],
 [1, 1, 0, 1, 1 ,1 ,1 ,1 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1],
 [1, 1, 0, 0, 1, 1, 1 ,1 ,0 ,1 ,1 ,0, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 0, 0],
 [1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1],
 [1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 0, 1, 1 ,1 ,1 ,0 ,1, 1, 1, 1, 1, 1, 1 ,1, 1 ,1],
 [1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1, 1],
 [1, 1, 1, 1, 1 ,1, 1, 1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1],
 [1, 1, 1, 1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1, 1, 1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1],
 [1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1, 1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1, 1],
 [1, 1, 1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1, 1, 1 ,1, 0, 1 ,1 ,1 ,1 ,1],
 [1, 1, 1, 1, 1, 1, 1, 1, 0, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1 ,1 ,0 ,1 ,1 ,1, 1],
 [1, 1 ,1 ,1 ,1 ,1 ,1, 1, 0, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1, 1 ,1 ,0, 1 ,1 ,1],
 [1 ,1 ,1 ,1 ,1 ,1 ,1, 1, 0, 1, 1 ,1 ,1 ,1, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1],
 [1, 1 ,1 ,0 ,1 ,1 ,1 ,1 ,0 ,0 ,1, 0, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1, 1, 0 ,0],
 [1, 1, 0, 0, 1, 1, 1 ,1 ,0 ,0 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1, 1, 1, 1, 0 ,0]]
)
"""

"""
A = np.array([[0 ,1 ,0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1 ,0 ,1 ,0, 0, 1],
 [1, 0, 1 ,0 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,1 ,0, 0, 0, 0, 1, 0, 1],
 [0, 1 ,0 ,1 ,1 ,0 ,0 ,0 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,1],
 [0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1 ,0],
 [0 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,0],
 [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1 ,1],
 [0 ,1 ,0 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0 ,0],
 [1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0 ,0],
 [0, 0 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0],
 [1, 0 ,1 ,1 ,1 ,0 ,0 ,1, 1, 0, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0],
 [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0 ,0],
 [0, 1, 0, 1, 0, 1, 0, 1, 1 ,1 ,0 ,0 ,1, 1, 1 ,1 ,1 ,1 ,0],
 [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1 ,1 ,1 ,1 ,1],
 [1, 0, 0 ,1 ,1 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,0],
 [0 ,0 ,0 ,1 ,1 ,0 ,0 ,1 ,1 ,1 ,0, 1, 1, 1 ,0 ,0 ,1 ,1 ,0],
 [1, 0 ,1 ,1 ,1 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1, 1, 0, 0, 1 ,1 ,0],
 [0, 1 ,0 ,1 ,1 ,1 ,0 ,0, 1, 1 ,0, 1 ,1 ,1 ,1 ,1 ,0 ,1 ,1],
 [0 ,0 ,0 ,1 ,1 ,1 ,0 ,0 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,0],
 [1, 1 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0]])
"""
for k in range(2,10):
    estimator = SpectralClustering(n_clusters=k,random_state=0,affinity='precomputed').fit_predict(A)
    Scores.append(metrics.silhouette_score(A, estimator, metric='euclidean'))
    print (estimator)
    Scores1.append(metrics.calinski_harabasz_score(A, estimator))
print(Scores)
# print(Scores1)
i = range(2, 11)
plt.xlabel('k')
plt.ylabel('value')
# plt.tick_params(labelsize=12)
# plt.plot(i,Scores,'g.-',i,Scores1,'b.-')
ln1, = plt.plot(i,Scores,'limegreen',linestyle='-')
ln2, = plt.plot(i,Scores1,'b*',linestyle='--')
plt.legend(handles=[ln1,ln2],labels=['calinski_harabasz_score','silhouette_score'],loc='upper right')
# plt.legend(handles=[ln2],labels=['silhouette_score'],loc='upper right')
plt.savefig(r"C:\\Users\\28708\\Desktop\\data_result2\\cc.svg", dpi=600,format="svg")
plt.show()



print (estimator)
"""
######Adult set
l = [0, 3, 0 ,2, 2 ,0, 2, 0 ,1 ,0, 3, 0, 0, 1, 0]
######find xiangtong elment suoyin place
nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']

for i in range(0, 4):
    elment_place = []
    name_list = []
    for index, nums in enumerate(l):
        if nums == i:
            elment_place.append(index)
    # print(elment_place)
    for j in range(0, len(elment_place)):
        name_list.append(nodes[elment_place[j]])
    print name_list
    """
"""
######Retail set
l = [0, 3, 0 ,2, 2 ,0, 2, 0 ,1 ,0, 3, 0, 0, 1, 0]
######find xiangtong elment suoyin place
nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']

for i in range(0, 4):
    elment_place = []
    name_list = []
    for index, nums in enumerate(l):
        if nums == i:
            elment_place.append(index)
    # print(elment_place)
    for j in range(0, len(elment_place)):
        name_list.append(nodes[elment_place[j]])
    print name_list
    """
"""
######TPC-E set

l = [2, 2, 2, 3, 2, 2, 2, 2, 1, 2, 0, 4, 2 ,2 ,2 ,2 ,2 ,2 ,2, 2, 2, 2, 2, 5]
######find xiangtong elment suoyin place
nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p','q',
'r','s','t','u','v','w','x']

for i in range(0, 6):
    elment_place = []
    name_list = []
    for index, nums in enumerate(l):
        if nums == i:
            elment_place.append(index)
    # print(elment_place)
    for j in range(0, len(elment_place)):
        name_list.append(nodes[elment_place[j]])
    print name_list
    """