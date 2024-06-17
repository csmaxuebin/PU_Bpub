import matplotlib.pyplot as plt
i = [0.1,0.3,0.5,0.7,0.9]
# """
######Adult set
Scores=[0.200552092,0.200104855,0.211740967,0.246717966,0.647692247]
Scores1=[0.322796627,0.327790581,0.341807508,0.379247873,0.772639295]
Scores2=[0.55860434,0.563605293,0.572554625,0.587132988,0.947947962]
# """
"""
#########TCP-E set
Scores=[0.532241477,0.538308714,0.543101899,0.608665211,0.75074939]
Scores1=[0.668045511,0.680504902,0.684336695,0.75074939,0.882548821]
Scores2=[0.882700404,0.887688813,0.883147641,0.912862139,0.962548821]
"""
"""
#####Retail set
Scores = [0.073466824, 0.072764374, 0.071157701, 0.081624314, 0.088622582]
Scores1 = [0.122228391, 0.121973248, 0.119520589, 0.128921182, 0.140817314]
Scores2 = [0.17740541, 0.178691203, 0.179032369, 0.181851591, 0.197125534]
Scores3 = [0.203181883, 0.205041656, 0.201903913, 0.211654546, 0.208357118]
# """
# """
plt.xlabel('f',fontsize=12)
plt.ylabel('AVD',fontsize=12)
plt.tick_params(labelsize=12)
# y_values=[x for x in x_values]
plt.ylim(0,1)
# plt.plot(i,Scores,'g.-',i,Scores1,'b.-')
ln1, = plt.plot(i,Scores,'g*',marker='s',markersize=10,markerfacecolor='none',linestyle='--')
ln2, = plt.plot(i,Scores1,'b*',marker='^',markersize=10,markerfacecolor='none',linestyle='--')
ln3, = plt.plot(i,Scores2,'r*',marker='o',markersize=10,markerfacecolor='none',linestyle='--')
# ln4, = plt.plot(i,Scores3,'y*',marker='d',markersize=10,markerfacecolor='none',linestyle='--')
# plt.legend(handles=[ln1,ln2,ln3,ln4],labels=['k=2','k=3','k=4','k=5'],loc='upper right',fontsize=14)
plt.legend(handles=[ln1,ln2,ln3],labels=['k=2','k=3','k=4'],loc='lower right',fontsize=14)
plt.savefig(r"C:\\Users\\28708\\Desktop\\data_result4\\avd_b.svg", dpi=600,format="svg")
plt.show()
# plt.savefig("C:\Users\\28708\\Desktop\\.png", dpi=600,format="png")