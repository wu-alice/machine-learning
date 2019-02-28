import kNN
group,labels = kNN.createDataSet()
print(kNN.classify0([0,0],group,labels,3))
print(kNN.classify0([1,2],group,labels,3))