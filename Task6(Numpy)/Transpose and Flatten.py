import numpy

n,m=map(int,input().split())
l=[]
for i in range(n):
    row=list(map(int,input().split()))
    l.append(row)

arr=numpy.array(l)    
print(numpy.transpose(arr))
print(arr.flatten())


