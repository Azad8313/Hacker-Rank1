# Enter your code here. Read input from STDIN. Print output to STDOUT
A=set(map(int,input().split()))
n=int(input())
count=0
for i in range(n):
    other_set=set(map(int,input().split()))
    if(A.issuperset(other_set)):
       count+=1
print(count==n)           

