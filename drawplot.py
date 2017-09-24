#-*-coding:utf8-*-
import matplotlib.pyplot as plt
def drawplot(dataset):
    fig=plt.figure(1)
    ax = fig.add_subplot(111)
    ax.scatter(dataset[:,1],dataset[:,0],c='r',marker='^')
    plt.show()