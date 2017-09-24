#-*-coding:utf8-*-
import numpy as np
def createdata(filename):
    file=open(filename)
    lines = file.readlines()
    rows=len(lines)
    #两个特征
    dataMatrix = np.zeros((rows,2))

    row = 0
    for line in lines:
        line = line.strip().split(' ')

        dataMatrix[row, :] = line[:]
        row += 1
    print dataMatrix
    file.close()
    return dataMatrix
