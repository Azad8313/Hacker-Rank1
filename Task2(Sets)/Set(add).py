# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
stamp=[]
for i in range(n):
    country=input()
    stamp.append(country)
distinct_country=set(stamp)
print(len(distinct_country))        
