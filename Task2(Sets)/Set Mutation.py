# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
A=set(map(int,input().split()))
n=int(input())
for i in range(n):
    cmd=input().split()
    other_set=set(map(int,input().split()))
    if cmd[0]=='intersection_update':
        A.intersection_update(other_set)
    elif cmd[0]=='update':
        A.update(other_set)
    elif cmd[0]=='symmetric_difference_update':
        A.symmetric_difference_update(other_set)                     
    elif cmd[0]=='difference_update':
        A.difference_update(other_set)
print(sum(A))            
