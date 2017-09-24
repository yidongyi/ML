#-*-coding:utf8-*-
import numpy as np
'''改进的欧氏距离'''
p=np.random.random(10)
q=np.random.random(10)
w=np.random.random(10)#权重


dpq=np.sqrt(np.dot((np.square(x-y)),w.T))
print dpq;


Spq=1.0/(1+beta*dpq);#相似度计算


