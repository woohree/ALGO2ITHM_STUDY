import sys
sys.stdin = open('B.txt')

'''
50분
1. 신기하게 보자마자 Union-Find 알고리즘이 생각남. 사이클을 이룰 수 있는 숫자끼리는 부모를
기억하는게 좋다고 생각됨
2. 그러다 부모를 찾던 중 두 수가 모두 같은 부모를 가르키고 있으면 사이클을 이루는 거라 생각됨
'''


# 특정 원소가 속한 집합을 찾기
def find(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
        return 0
    elif a == b:  # 2번. a와 b의 부모가 같은 경우
        return 1
    else:
        parent[a] = b
        return 2


n, m = map(int, input().split())
parent = list(range(n))
flag = 0
for i in range(1, m+1):
    a, b = map(int, input().split())
    if union(parent, a, b) == 1:
        flag = 1
        print(i)
        break
if not flag:
    print(0)
