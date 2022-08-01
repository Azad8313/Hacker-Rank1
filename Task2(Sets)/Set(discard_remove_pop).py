n = int(input())
s = set(map(int, input().split()))
#print(s)
cmd_number=int(input())
for i in range(cmd_number):
    cmd=input().split()
#    print(cmd)
    if cmd[0]=='pop':
        s.pop()
    elif cmd[0]=='remove':
        s.remove(int(cmd[1]))        
    elif cmd[0]=='discard':
        s.discard(int(cmd[1]))
print(sum(s))                
