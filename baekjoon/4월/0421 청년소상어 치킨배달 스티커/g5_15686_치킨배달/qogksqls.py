import sys
sys.stdin = open('B.txt')

# 치킨집 많이 안 나올거 같아서 느낌이어서 조합 사용. 다행히 통과
from itertools import combinations

N, M = map(int, sys.stdin.readline().rstrip().split())
city = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

# 치킨집과 집의 위치 찾는 과정
chickens, homes = [], []
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chickens.append((i, j))
        elif city[i][j] == 1:
            homes.append((i, j))

# 치킨집이 N개씩 들어간 조합
comb = combinations(chickens, M)

my_min = 99999999
for c in comb:
    # 도시의 치킨 거리
    chicken_dist_total = 0
    
    # 집에서 치킨집 별로 치킨 거리 비교한 다음 최소 값을 치킨 거리로 저장
    for home in homes:
        chicken_dist = 2 * N
        for chicken in c:
            chicken_dist_temp = abs(home[0] - chicken[0]) + abs(home[1] - chicken[1])
            chicken_dist = min(chicken_dist, chicken_dist_temp)
        # 치킨 거리를 도시의 치킨 거리에 누적
        chicken_dist_total += chicken_dist
    
    # 조합 별로 도시의 치킨 거리가 가장 작은 값을 my_min 에 저장
    my_min = min(my_min, chicken_dist_total)

print(my_min)

'''
# 1등 코드: 104ms
import sys
N,M = map(int,sys.stdin.readline().split())
city = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

# 똑같이 집과 치킨집의 위치 저장하는 list
house = []
chicken = []
for i in range(N):
  for j in range(N):
    if city[i][j] == 2:
      chicken.append((i,j))
    elif city[i][j] == 1:
      house.append((i,j))

# 일단 집별 치킨거리를 다 구함
chicken_distance = []
for i in range(len(house)):
  chicken_distance.append([])
  for j in range(len(chicken)):
    chicken_distance[-1].append((abs(house[i][0]-chicken[j][0]) + abs(house[i][1]-chicken[j][1]),j))
  chicken_distance[-1].sort(key = lambda x: x[0])

ans = 1000000000
def city_chicken_distance():
  global ans
  a = 0
  for i in chicken_distance:
    for j in i:
      # 살아남은 치킨집이라면 그 치킨거리 값을 a에 더함
      if j[1] in survived:
        a += j[0]
        break
    # 가지치기
    if a >= ans:
      return
  ans = min(ans,a)

def open(M,n):
  if M == 0:
    city_chicken_distance()
  for i in range(n,len(chicken)):
    if i not in survived:
      # survived에 치킨집을 저장하면서 open 함수를 M이 0일 될 때까지 재귀 돌림
      survived.add(i)
      open(M-1,i+1)
      survived.remove(i)

survived = set()
open(M,0)

# 조합 쓰지 않고 재료들을 미리 구해놓고 dfs한 느낌이랄까
print(ans)
'''
