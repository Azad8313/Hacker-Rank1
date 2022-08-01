if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    x1=[a for a in range(x+1)]
    y1=[a for a in range(y+1)]
    z1=[a for a in range(z+1)]
    perm=[[i,j,k] for i in x1 for j in y1 for k in z1]
    r=[l for l in perm if sum(l)!=n]
    print(r)