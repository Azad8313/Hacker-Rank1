# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
eng_paper=set(map(int,input().split()))
b=int(input())
fren_paper=set(map(int,input().split()))
total_student=eng_paper.intersection(fren_paper)
print(len(total_student))
