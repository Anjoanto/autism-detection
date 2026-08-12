import numpy as np
import statistics
import csv

data = np.loadtxt(fname='test.csv', delimiter=',')
x = []
y = []
for i in range(len(data)):
    for j in range(2):
        if j == 0:
            x.append(data[i][j])
        else:
            y.append(data[i][j])
print("x axis:", x)
print("y axis:", y)


c = len(y) / 21
d = np.array_split(y, c)
b = len(x) / 21
a = np.array_split(x, b)

arr1=[]
arr2=[]




for i in a:
    arr1.append(int (statistics.mean(i)))

for j in d:
    arr2.append(int(statistics.mean(j)))


print("x",arr1)
print("y",arr2)
g = open("free.csv", "a", newline="")
# g = np.loadtxt(fname='free.csv', delimiter=',')

arr1len = len(arr1)
arr2len = len(arr2)

#print("len",arr2len,arr2len)

for i in range(0,arr1len):
    writer = csv.writer(g)
    writer.writerow([arr1[i],arr2[i]])
g.close()
exec(open('graph.py').read())
