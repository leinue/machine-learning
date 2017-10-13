#-*- coding: UTF-8 -*-

import knn
import matplotlib
import matplotlib.pyplot as plt

group,labels = knn.createDataset()

result = knn.classify0([2, 2], group, labels, 3)
print result

# mat, vec = knn.file2matrix('./datingTestSet2.txt')
# print mat

# fig = plt.figure()
# ax = fig.add_subsplot(111)
# ax.scatter(vec[:,1], vec[:,2])
# plt.show()
# norMat, ranges, minVals = knn.autoNorm(mat)

# print norMat
# print ranges
# print minVals

# knn.datingClassTest()

knn.handwritingClassTest()

