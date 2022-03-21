# 30분

import sys
sys.stdin = open('B.txt')

from collections import deque

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    soldier = deque(map(int, sys.stdin.readline().rstrip().split()))
    # 첫번째 값 빼주려고 deque 사용
    N = soldier.popleft()
    # 정렬하는데 sort 함수는 deque 이랑 호환 안됨
    soldier = sorted(soldier)

    temp = max_troop = max_soldiers = 1
    for i in range(len(soldier) - 1):
        if soldier[i] == soldier[i+1]:
            temp += 1
            # 최대 값 저장
            if max_soldiers < temp:
                max_troop = soldier[i]
                max_soldiers = temp
        # temp 만 초기화
        elif soldier[i] != soldier[i+1]:
            temp = 1

    if max_soldiers > N // 2:
        print(max_troop)
    else:
        print('SYJKGW')
