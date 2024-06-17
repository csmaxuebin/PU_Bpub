import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif']=['SimHei']
labels = ["0.1","0.3","0.5","0.7","0.9"]
"""
######Adult set


y1 = [632.3,1297.5,2030.1,3936.2,4631.4]

y2 = [208.6,456.1,708.7,948.3,1234.8]
y3=[316.25,649.75,1015.157,1354.38,1794.86]
y4=[315,640.32,1003.16,1353.09,1783.90]
"""
"""
######TCP-E set


y1 = [387.6,1001.3,1654.6,3195.5,3854.8]
y2 = [314.6,651.7,981.7,1494.8,1912.5]
y3=[350,750.35,1200.467,1700,2200.821]
y4=[345,745,1156,1680.983,2107.45]
"""
# """
######Retail set

y1=[108.56,224.40,353.10,386.36,416.69]
y2=[54.01,112.90,160.36,204.93,228.37]
y3=[70,141.5,222,281.5,349.5]
y4=[65,127.5,191,256.5,316.5]
# """
# """
x = np.arange(len(labels))
width = 0.2

fig, ax = plt.subplots()
rects1 = ax.bar(x - width*2, y1, width, label='Lopub',color='grey',edgecolor='black',lw=.8)
rects2 = ax.bar(x - width+0.01, y2, width, label='PU_Bpub',color='w',edgecolor='black',hatch="....",lw=.8)
rects3 = ax.bar(x + 0.02, y3, width, label='DR_LoCop',color='w',edgecolor='black',hatch="/////",lw=.8)
rects4 = ax.bar(x + width+ 0.03, y4, width, label='LoCop',color='w',edgecolor='black',hatch=" ",lw=.8)
# rects5 = ax.bar(x + width*2 + 0.04, e, width, label='e')


plt.ylim(0,500)
ax.set_ylabel('Running Time(s)', fontsize=16)
ax.set_xlabel('f', fontsize=16)

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):

    for rect in rects:
        height = rect.get_height()


autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)


fig.tight_layout()
plt.savefig(r"C:\\Users\\28708\\Desktop\\data_result2\\time3.svg", dpi=600,format="svg")
plt.show()

