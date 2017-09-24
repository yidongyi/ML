#-*-coding:utf8-*-
from createdata import createdata
from drawplot import drawplot

if __name__=="__main__":

    filename = 'text.txt'
    dataMatrix = createdata(filename)
    drawplot(dataMatrix)