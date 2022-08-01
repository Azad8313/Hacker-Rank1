# Enter your code here. Read input from STDIN. Print output to STDOUT
test_case=int(input())
for i in range(test_case):
    a=int(input())
    A=set(map(int,input().split()))
    b=int(input())
    B=set(map(int,input().split()))
    print(A.issubset(B))
