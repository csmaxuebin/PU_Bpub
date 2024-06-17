



import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif']=['SimHei']
"""
######Adult set
labels = ['1', '2','3']

y1=[0.17,0.25,0.37]
y2=[0.14,0.21,0.34]
y3=[0.07,0.145,0.27]
y4=[0.06,0.14,0.26]
"""
"""
######TCP-E set
labels = ['1', '2','3']

y1=[0.3,0.550998868,0.69]
y2=[0.25,0.5,0.67]
y3=[0.2,0.351,0.6]
y4=[0.19,0.345,0.59]
"""
# """
######Retail set
labels = ['2', '3','5']
y1=[0.23,0.35,0.38]
y2=[0.071157701,0.119520589,0.201903913]
y3=[0.075,0.14,0.18]
y4=[0.065,0.12,0.16]
# """
x = np.arange(len(labels))
width = 0.2

fig, ax = plt.subplots()
rects1 = ax.bar(x - width*2, y1, width, label='Lopub',color='grey',edgecolor='black',lw=.8)
rects2 = ax.bar(x - width+0.01, y2, width, label='PU_Bpub',color='w',edgecolor='black',hatch="...",lw=.8)
rects3 = ax.bar(x + 0.02, y3, width, label='DR_LoCop',color='w',edgecolor='black',hatch="///",lw=.8)
rects4 = ax.bar(x + width+ 0.03, y4, width, label='LoCop',color='w',edgecolor='black',hatch=" ",lw=.8)
# rects5 = ax.bar(x + width*2 + 0.04, e, width, label='e')


plt.ylim(0,0.5)
ax.set_ylabel('AVD', fontsize=16)
ax.set_xlabel('k', fontsize=16)
plt.tick_params(labelsize=14)
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):

    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3))

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)


fig.tight_layout()
plt.savefig(r"C:\Users\\28708\\Desktop\\data_result4\\avdk_ccc.svg", dpi=600,format="svg")
plt.show()

