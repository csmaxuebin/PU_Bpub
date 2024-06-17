import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
i = [0.1,0.3,0.5,0.7,0.9]
"""
######Adult set
Scores=[0.716911765,0.716,0.717,0.7169,0.7169]
Scores1=[0.672,0.67,0.668,0.66,0.533088235]
Scores2=[0.673,0.673,0.67279,0.6723,0.569852941]
Scores3=[0.698,0.69,0.684,0.675,0.665]
Scores4=[0.69,0.683,0.68,0.67,0.66]
"""
# """
#########TCP-E set
Scores=[0.6805,0.68,0.6805,0.68,0.6805]
Scores1=[0.5525,0.55,0.54,0.52632,0.43]
Scores2=[0.67,0.6433333333333333,0.6366666666666667,0.636,0.512]
Scores3=[0.6781,0.66703,0.65685,0.6465,0.5866]
Scores4=[0.673,0.6637,0.64967,0.63665,0.5762]
# """
"""
#####Retail set
Scores = [0.844230769, 0.844, 0.844230769, 0.844, 0.844230769]
Scores1 = [0.7326923076923075, 0.715, 0.69, 0.6211538461538462, 0.61]
Scores2 = [0.7942307692307693, 0.7855769230769232, 0.7528846153846153, 0.67, 0.661538462]
Scores3 = [0.8,0.793,0.786,0.77,0.75]
Scores4 = [0.794,0.781,0.77,0.7669,0.7425]
# """
# """
plt.xlabel('f',fontsize=12)

plt.ylabel('Classification Rate',fontsize=12)
plt.ylim(0.4,0.7)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
# plt.rcParams['figure.figsize'] = (6.0, 5.0)
# plt.plot(i,Scores,'g.-',i,Scores1,'b.-')
# ln1, = plt.plot(i,Scores,color='#63BEF5',marker='s',markerfacecolor='none',linestyle='-',markersize=10)
# ln2, = plt.plot(i,Scores1,color='#3CFF3C',marker='^',markerfacecolor='none',linestyle='-',markersize=10)
# ln3, = plt.plot(i,Scores2,color='#F99C5E',marker='o',markerfacecolor='none',linestyle='-',markersize=10)
# ln4, = plt.plot(i,Scores3,color='#F2E423',marker='d',markerfacecolor='none',linestyle='-',markersize=10)
# ln5, = plt.plot(i,Scores4,color='#E26FFF',marker='x',linestyle='-')
ln1, = plt.plot(i,Scores,'g*',marker='s',markerfacecolor='none',linestyle='--',markersize=10)
ln2, = plt.plot(i,Scores1,'b*',marker='^',markerfacecolor='none',linestyle='--',markersize=10)
ln3, = plt.plot(i,Scores2,'r*',marker='o',markerfacecolor='none',linestyle='--',markersize=10)
ln4, = plt.plot(i,Scores3,'y*',marker='d',markerfacecolor='none',linestyle='--',markersize=10)
ln5, = plt.plot(i,Scores4,'m*',marker='x',linestyle='--',markersize=10)
plt.legend(handles=[ln1,ln2,ln3,ln4,ln5],labels=['Non Privacy','Lopub','PU_Bpub','DR_LoCop','LoCop'],loc='lower left',fontsize=12)
plt.savefig(r"C:\\Users\\28708\\Desktop\\data_result2\\SVMa.svg", dpi=600,format="svg")
plt.show()
# """
# """
"""
"""
"""
#########Adult set
Scores = [0.689, 0.685, 0.689, 0.685, 0.68]
Scores1 = [0.5036, 0.485, 0.4663, 0.455, 0.42647058823529416]
Scores2 = [0.53,0.51283,0.50915,0.49333,0.43014705882352944 ]
Scores3 = [0.54,0.53,0.52,0.51,0.50]
Scores4 = [0.535,0.522,0.515,0.50,0.49]

"""
"""
#####TCP-E set
Scores = [0.59, 0.59, 0.59, 0.59, 0.59]
Scores1 = [0.31,0.284, 0.2333333333333, 0.21333333, 0.18]
Scores2 = [0.35,0.298, 0.26, 0.22499999,0.187 ]
Scores3 = [0.352,0.3245,0.3045,0.276,0.215]
Scores4 = [0.345,0.3036,0.28701,0.254,0.21]
"""
"""
#######Retail set
Scores = [0.82, 0.8207, 0.82, 0.8204, 0.82]
Scores1 = [0.7490384615384615, 0.7221153846153845, 0.71, 0.6365384615384616, 0.6153848]
Scores2 = [0.7865384615384616,0.7798076923076922,0.7677884615384616,0.6754807692307694,0.6543269230769231]
Scores3 = [0.798,0.783,0.77,0.745,0.70]
Scores4 = [0.79,0.7781,0.76,0.74,0.68]
"""
"""
plt.xlabel('f',fontsize=12)
plt.ylabel('Classification Rate',fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.ylim(0.3,0.7)
ln1, = plt.plot(i,Scores,'g*',marker='s',markerfacecolor='none',linestyle='--',markersize=10)
ln2, = plt.plot(i,Scores1,'b*',marker='^',markerfacecolor='none',linestyle='--',markersize=10)
ln3, = plt.plot(i,Scores2,'r*',marker='o',markerfacecolor='none',linestyle='--',markersize=10)
ln4, = plt.plot(i,Scores3,'y*',marker='d',markerfacecolor='none',linestyle='--',markersize=10)
ln5, = plt.plot(i,Scores4,'m*',marker='x',linestyle='--')

plt.legend(handles=[ln1,ln2,ln3,ln4,ln5],labels=['Non Privacy','Lopub','PU_Bpub','DR_LoCop','LoCop'],loc='lower left',fontsize=12)
plt.savefig(r"C:\\Users\\28708\\Desktop\\data_result2\\RFb.svg", dpi=600,format="svg")
plt.show()
"""