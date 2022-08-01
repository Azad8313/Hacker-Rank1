# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
eng_paper=set(map(int,input().split()))
n1=int(input())
fren_paper=set(map(int,input().split()))
#print(eng_paper)
#print(fren_paper)
total_std=eng_paper | fren_paper ##'|' inplace of '.union'
print(len(total_std))
