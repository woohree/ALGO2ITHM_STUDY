# dp?

import sys
sys.stdin = open('B.txt')


def get_answer(ans, ind):
    for i in range(N-1, -1, -1):
        check = 0
        if ans and counseling[i][0] + i <= N:
            for j in range(len(ind)):
                if counseling[i][0] + i > ind[j]:
                    temp = 0

                    for k in range(j, len(ind)):
                        temp += ans[k]

                    if counseling[i][1] > temp:
                        a = len(ind)
                        for _ in range(a - j):
                            answer_bin.append(ans.pop())
                            index_bin.append(ind.pop())
                        ans.append(counseling[i][1])
                        ind.append(i)
                        get_answer(answer_bin, index_bin)

                    check += 1
                    break

        if counseling[i][0] + i <= N:
            if check == 0:
                ans.append(counseling[i][1])
                ind.append(i)


N = int(input())
counseling = [list(map(int, input().split())) for _ in range(N)]

answer = []
index = []
answer_bin = []
index_bin = []
get_answer(answer, index)

print(sum(answer))
