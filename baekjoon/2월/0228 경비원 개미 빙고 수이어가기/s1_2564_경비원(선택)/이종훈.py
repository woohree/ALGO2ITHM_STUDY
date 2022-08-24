import sys
sys.stdin = open('input.txt')

x,y = map(int,input().split())


n = int(input())

mapl=[[],[],[],[]]
cntl=0
mapr=[[],[],[],[]]
cntr=0

for _ in range(x):
    mapl[0] += [[0,cntl]]
    cntl += 1
for _ in range(y-1):
    mapl[2] += [[0, cntl]]
    cntl += 1
for _ in range(x-2):
    mapl[1] += [[0, cntl]]
    cntl += 1
for _ in range(y-1):
    mapl[3] += [[0, cntl]]
    cntl += 1

for _ in range(x):
    mapr[0] += [[0, cntr]]
    cntr += 1
for _ in range(y - 1):
    mapr[3] += [[0, cntr]]
    cntr += 1
for _ in range(x - 2):
    mapr[1] += [[0, cntr]]
    cntr += 1
for _ in range(y - 1):
    mapr[2] += [[0, cntr]]
    cntr += 1



print(mapl)
print(mapr)

coodinate = []
for _ in range(n):
    coodinate += [list(map(int,input().split()))]  #왜이래?

