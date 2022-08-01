# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
a=set(map(int,input().split()))
m=int(input())
b=set(map(int,input().split()))
result=list(a.symmetric_difference(b))
result.sort()
for i in result:
    print(i)
