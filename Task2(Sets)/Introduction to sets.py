def average(array):
    array=set(array)
    sum=0
    for j in array:
        sum+=j          ##sum(array)/len(array)
    avg=sum/len(array)    
    return avg

'''set1=set()  
n=int(input())
for i in range(n):
    element=int(input())
    set1.add(element)
result=average(set1)
print(result)       
'''
if __name__ == '__main__':