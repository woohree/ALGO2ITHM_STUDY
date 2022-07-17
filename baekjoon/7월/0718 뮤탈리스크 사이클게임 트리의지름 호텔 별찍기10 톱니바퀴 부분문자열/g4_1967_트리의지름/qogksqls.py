import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('B.txt')

'''
65분
1. 원래는 부모노드에 (자식번호, 가중치)를 저장하는 방식으로 시작. 단방향이다.
2. 루트노드부터 맨 끝까지 자식들 중에 가장 큰 두 놈을 꼽아 더해줘서 제일 큰 값을 출력.
3. 하지만 36% 시간초과. 모든 노드 다 살펴봐서 그런가봄
4. 구글링..
5. 양방향 그래프를 구한다. 
6. 루트에서 가장 먼 놈을 찾는다.
7. 가장 먼놈에서부터 가장 먼 놈을 찾아 최대 가중치를 구한다.
'''


def dfs(x, num):
    for next_, w in graph[x]:
        if distance[next_] == -1:
            distance[next_] = num + w
            dfs(next_, num + w)


n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n + 1)]  # 5번
for _ in range(n-1):
    p, c, w = map(int, sys.stdin.readline().rstrip().split())
    graph[p].append((c, w))
    graph[c].append((p, w))

# 6번
distance = [-1] * (n+1)
distance[1] = 0
dfs(1, 0)

# 7번
s = distance.index(max(distance))
distance = [-1] * (n+1)
distance[s] = 0
dfs(s, 0)
print(max(distance))


'''
def dfs(x, num):
    global temp
    if not trees[x]:
        temp = max(temp, num)
        return
    for k in range(len(trees[x])):
        dfs(trees[x][k][0], num + trees[x][k][1])


n = int(sys.stdin.readline().rstrip())
trees = [[] for _ in range(n + 1)]  # 5번
for _ in range(n - 1):
    p, c, w = map(int, sys.stdin.readline().rstrip().split())
    trees[p].append((c, w))
print(trees)
my_max = 0
for i in range(1, n+1):
    if trees[i]:
        temp_list = []
        for j in range(len(trees[i])):
            temp = 0
            dfs(trees[i][j][0], trees[i][j][1])
            if len(temp_list) < 2:  # sort 안쓰려고 stack 쓰는중
                if temp_list:
                    if temp_list[0] < temp:
                        a = temp_list.pop()
                        temp_list.append(temp)
                        temp_list.append(a)
                    else:
                        temp_list.append(temp)
                else:
                    temp_list.append(temp)
            elif temp_list[1] < temp:
                temp_list.pop()
                if temp_list[0] < temp:
                    a = temp_list.pop()
                    temp_list.append(temp)
                    temp_list.append(a)
                else:
                    temp_list.append(temp)  # 여기까지

        if len(temp_list) >= 2:
            my_max = max(my_max, temp_list[0] + temp_list[1])
        else:
            my_max = max(my_max, temp_list[0])
    print(temp_list)

print(my_max)
'''