import numpy
n,m=map(int,input().split())
l1=[]
l2=[]
for i in range(n):
    ele=list(map(int,input().split()))
    l1.append(ele)
for i in range(n):
    ele=list(map(int,input().split()))
    l2.append(ele)
        
A=numpy.array(l1)
B=numpy.array(l2)

print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)
print(A**B)
