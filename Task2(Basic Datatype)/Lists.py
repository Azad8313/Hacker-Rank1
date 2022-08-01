if __name__ == '__main__':
    N = int(input())
    l=[]
    for i in range(N):
        cmd=input().split()
        if cmd[0]=='insert':
            l.insert(int(cmd[1]),int(cmd[2]))
        elif cmd[0]=='print':
            print(l)
        elif cmd[0]=='remove':
            l.remove(int(cmd[1]))
        elif cmd[0]=='append':
            l.append(int(cmd[1]))
        elif cmd[0]=='sort':
            l.sort()            
        elif cmd[0]=='pop':
            l.pop()
        elif cmd[0]=='reverse':
            l.reverse()        
