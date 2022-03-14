# 40분

import sys
sys.stdin = open('B.txt')


def find_kinship():
    global count, m, a, b, check
    for i in range(m):
        # relations의 i번 째 값에서 a를 찾은 경우
        if relations[i][0] == a:
            # 촌수 카운트를 1 더한다.
            count += 1
            # a의 부모가 b인 경우, check에 1 더하고 return
            if b == relations[i][1]:
                check += 1
                return
            # 아니면 a를 부모 숫자로 바꾸고, 해당 관계를 temp에 옮겼다가 부모 관계 수인 m을 1 빼준다.
            a = relations[i][1]
            temp.append(relations.pop(i))
            m -= 1

            find_kinship()
            # 함수를 빠져나왔을 때, check가 1이라면 바로 return
            if check == 1:
                return
            # b를 못 찾은 경우
            # 다시 relations과 m, a를 이전 값으로 돌린다.
            relations.append(temp.pop())
            m += 1
            a = relations[-1][0]

        # relations의 i번 째 값의 두번 째에서 a를 찾은 경우
        # 위의 식 반복함
        elif relations[i][1] == a:
            count += 1
            if b == relations[i][0]:
                check += 1
                return
            a = relations[i][0]
            m -= 1
            temp.append(relations.pop(i))
            find_kinship()
            if check == 1:
                return
            relations.append(temp.pop())
            m += 1
            a = relations[-1][1]

    # for문을 돌았는데 b를 못찾은 경우 이므로 count에 1을 빼면서 return
    if check == 0:
        count -= 1
        return


n = int(input())
a, b = map(int, input().split())
m = int(input())
relations = [list(map(int, input().split())) for _ in range(m)]

# 촌수를 계산할 count, 친척 관계임을 체크할 check
count = 0
check = 0
temp = []
find_kinship()

print(count)
