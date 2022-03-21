import sys
sys.stdin = open('M.txt')

# set, count 사용 -> 메모리 초과
"""
def war():
    for i in range(N):
        half = lands[i] / 2
        # 땅에 배치된 군대의 번호
        army_set = set(soldiers[i])
        # 군대별 병사의 숫자 세기
        for j in army_set:
            if soldiers[i].count(j) > half:
                print(j)
                break
        else:
            print('SYJKGW')
"""

# set, count 사용, 반복문 줄이기 -> 시간 초과
"""
def war_two():
    half = inputs[0] / 2
    army_set = set(inputs[1:])

    for j in army_set:
        cnt = inputs.count(j)
        if j == inputs[0]:
            cnt -= 1
        if cnt > half:
            print(j)
            break
    else:
        print('SYJKGW')
"""


# dict 사용 -> 통과
def war_three():
    army = {}
    for i in range(len(inputs)):
        if i == 0:
            half = inputs[i] / 2
        else:
            if inputs[i] in army:
                army[inputs[i]] += 1
                if army[inputs[i]] > half:
                    return inputs[i]
            else:
                army[inputs[i]] = 1
    else:
        return 'SYJKGW'


# 땅의 개수 N
N = int(input())
# lands = []      # 땅에 배치된 병사의 수
# soldiers = []   # 땅에 배치된 병사의 군대 번호
for n in range(N):
    inputs = list(map(int, input().split()))
    # lands.append(inputs[0])
    # soldiers.append(inputs[1:])

    # war_two()
    print(war_three())
