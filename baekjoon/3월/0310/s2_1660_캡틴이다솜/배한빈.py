# 약 180분
# 역시나 문제 이해가 오래 걸렸다...
# 인풋 91에서 죽어라 84만 뺐다... 절대 2가 안 나 오 더 라

import sys
sys.stdin = open('B.txt')

N = int(input())

tetrahedrons = []
temp = cannonball = 0
i = 1
n = N
# N의 크기에 따라 나올 수 있는 정사면체 값(대포알의 수)을 list에 입력
while n != 0:
    temp += i

    if cannonball + temp > n:
        n -= cannonball
        break

    else:
        cannonball += temp
        tetrahedrons.append(cannonball)
        tetrahedrons.append(cannonball)
        i += 1

# [1, 1, 4, 4, 10, 10, 20, 20, 35, 35, 56, 56, 84, 84 ...]
# 79 -> 35, 20, 20 ,4

k = 0
my_min = 100
# 최솟값을 구하기 위한 코드
while k != len(tetrahedrons):

    k += 1
    m = N
    count = 0

    while m != 0:
        for j in range(len(tetrahedrons) - k, -1, -1):
            if m - tetrahedrons[j] >= 0:
                m -= tetrahedrons[j]
                count += 1
                # 백트래킹
                if count == my_min:
                    break

    if my_min > count:
        my_min = count

print(my_min)
