# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
eng_paper=set(map(int,input().split()))
b=int(input())
fren_paper=set(map(int,input().split()))
eng_paper_student=eng_paper.difference (fren_paper)
print(len(eng_paper_student))
