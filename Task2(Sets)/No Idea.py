# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
array=list(map(int,input().split()))
A=set(map(int,input().split()))
B=set(map(int,input().split()))
Happyness=0
for i in array:
    if i in A:
        Happyness+=1
    elif i in B:
        Happyness-=1 
print(Happyness)        
                
