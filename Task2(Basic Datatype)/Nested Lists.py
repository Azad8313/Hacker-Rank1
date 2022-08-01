if __name__ == '__main__':
    marks=[]
    total=[]
    name_list=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marks.append(score)
        total.append([name,score])
    dup_remove=list(set(marks))
    dup_remove.sort()
    for name,score in total:
        if score==dup_remove[1]:
            name_list.append(name)
    name_list.sort()     
    for  i in name_list:
        print(i)
