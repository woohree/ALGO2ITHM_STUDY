'''# n = 10
# info = [0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 2]

n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]


def dfs(arrow, start):
    global my_max, result
    if start == -1:
        APEACH, RYAN = 0, 0
        for j in range(11):
            if info[j] != 0 and info[j] >= RYAN_info[j]:
                APEACH += 10 - j
            if RYAN_info[j] > info[j]:
                RYAN += 10 - j
        if my_max < RYAN - APEACH:
            my_max = RYAN - APEACH
            result = RYAN_info[:]
            result[10] += arrow
        return

    for i in range(start, -1, -1):
        if arrow > info[i]:
            RYAN_info[i] += info[i] + 1
            dfs(arrow - (info[i] + 1), i - 1)
            RYAN_info[i] -= info[i] + 1


RYAN_info = [0] * 11
my_max = 0
result = [-1]
dfs(n, 10)

print(result)
'''

def solution(n, info):
    def dfs(RYAN, arrow, s, RYAN_info):
        global my_max

        if s == 11:
            APEACH = 0
            for i in range(11):
                if info[i] != 0 and info[i] >= RYAN_info[i]:
                    APEACH += 10 - i

            if my_max <= RYAN - APEACH:
                my_max = RYAN - APEACH
                ryan_info = RYAN_info[:]
                ryan_info[10] += arrow
                result.append(ryan_info)
                return

        for i in range(s, 11):
            if arrow > info[i]:
                RYAN_info[i] += info[i] + 1
                dfs(RYAN + 10 - i, arrow - (info[i] + 1), i + 1, RYAN_info)
                RYAN_info[i] -= info[i] + 1
            else:
                RYAN_info[i] += arrow
                dfs(RYAN, 0, i + 1, RYAN_info)
                RYAN_info[i] -= arrow

    global my_max, RYAN
    dfs(RYAN, n, 0, RYAN_info)

    if result:
        print(result[-1])
        return result[-1]
    else:
        return [-1]


my_max, RYAN = 0.1, 0
RYAN_info = [0] * 11
result = []

solution(10, [0,0,0,0,0,0,5,5,5,5,2])
