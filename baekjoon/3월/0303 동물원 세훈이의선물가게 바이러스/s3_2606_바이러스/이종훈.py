import sys
sys.stdin=open('input.txt')

def virus(n):
    global summ
    if tree[n][0] == 0: #visited인지 확인
        tree[n][0] = 1
        summ += 1 #감염시킬때마다 summ에 +1

        for i in tree[n]:
            virus(i) #가지고 있는 모든 index에 바이러스를 퍼트림


C = int(input())
N = int(input())
network = []
for _ in range(N):
    network += [list(map(int, input().split()))]



tree = []
for _ in range(C + 1):
    tree += [[0]]

for lis in network: #리스트 0번에 있는 tree index에 1번을 추가, 반대로 리스트 1번에 있는 tree index에 0을 추가
    tree[lis[0]] += [lis[1]]
    tree[lis[1]] += [lis[0]]
summ = 0
virus(1) #1번을 통해 바이러스를 퍼트리면
print(summ - 1)