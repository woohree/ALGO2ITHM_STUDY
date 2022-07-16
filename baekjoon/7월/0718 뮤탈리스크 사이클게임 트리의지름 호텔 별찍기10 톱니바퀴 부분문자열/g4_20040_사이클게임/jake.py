import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
# 부모 노드를 점검하기 위해 부모 노드를 설정(임의대로 0~n까지)
parents = [i for i in range(n)]
ans = 0

# 제일 조상 노드를 찾음
def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]

# 부모 노드가 다르다면 합침(작은 수 쪽으로)
# 부모 노드가 같은 것이라면 답이므로 중단
def union(x, y, indx):
    global ans
    x = find(x)
    y = find(y)
    print(x, y)
    if x != y:
        parents[max(x,y)] = min(x,y)
    elif ans == 0:
        ans = indx

for i in range(m):
    a, b = map(int, input().split())
    union(a, b, i + 1)

print(ans)