
# coding: utf-8

# In[5]:

from random import *
from matplotlib import pyplot

rand = Random()
rand.seed(0)
vari = 0.2
x1num = 100
x1 = [rand.normalvariate(2, vari) for i in range(0, x1num)]
y1 = [rand.normalvariate(2, vari) for i in range(0, x1num)]
l1 = [0 for i in range(0, x1num)]

x2num = 100
x2 = [rand.normalvariate(1, vari) for i in range(0, x2num)]
y2 = [rand.normalvariate(1, vari) for i in range(0, x2num)]
l2 = [1 for i in range(0, x2num)]

x3num = 100
x3 = [rand.normalvariate(1, vari) for i in range(0, x2num)]
y3 = [rand.normalvariate(2, vari) for i in range(0, x2num)]
l3 = [2 for i in range(0, x2num)]

x = x1 + x2 + x3
y = y1 + y2 + y3
label = l1 + l2 + l3
total = x1num + x2num + x3num

zx = [0.2, 0.3, 0.4]
zy = [0.2, 0.3, 0.4]
colors = ['red', 'green', 'blue']
pyplot.scatter(x, y, color='black', alpha=0.8)
pyplot.scatter(zx, zy, color=colors, s=250, alpha=0.8)
pyplot.show()

dis_label = [0 for i in range(total)]
for n in range(100):
    for i in range(total):
        minj = mind = -1
        for j in range(len(zx)):
            dis = (x[i] - zx[j]) ** 2 + (y[i] - zy[j]) ** 2
            if minj == -1 or dis < mind:
                minj = j
                mind = dis
        dis_label[i] = minj
    data_colors = [colors[l] for l in dis_label]
    '''
    pyplot.scatter(x, y, color=data_colors, alpha=0.8)
    pyplot.scatter(zx, zy, color=colors,s=250, alpha=0.8)
    pyplot.show()
    '''
    
    for k in range(len(zx)):
        newx = zx[k]
        newy = zy[k]
        N = 1
        for i in range(total):
            if dis_label[i] == k:
                N += 1
                newx += x[i]
                newy += y[i]
        zx[k] = newx*1.0/N
        zy[k] = newy*1.0/N
pyplot.scatter(x, y, color=data_colors, alpha=0.8)
pyplot.scatter(zx, zy, color=colors,s=250, alpha=0.8)
pyplot.show()

