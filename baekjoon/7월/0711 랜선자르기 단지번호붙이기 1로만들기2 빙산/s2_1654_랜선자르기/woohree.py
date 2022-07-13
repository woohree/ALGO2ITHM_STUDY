import sys
sys.stdin = open('L.txt')


K, N = map(int, input().split())
lines = [int(sys.stdin.readline().rstrip()) for _ in range(K)]
# print(lines)
left, right = 1, max(lines)

while left <= right:            # 자를 랜선의 길이를 찾는 이진탐색
    mid = (left+right) // 2     # 자를 랜선의 길이
    cuts = 0                    # 자른 랜선의 갯수
    for line in lines:          # 랜선 돌면서,
        cuts += line // mid     # 해당 랜선을 잘라 갯수를 더해줌
    if cuts >= N:               # N개보다 많다면, 더 긴 길이가 가능한 지 찾음
        left = mid + 1
    else:                       # 적다면, 더 짧은 길이를 찾음
        right = mid - 1
print(right)