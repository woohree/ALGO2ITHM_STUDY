import sys
sys.stdin = open('M.txt')


def z(n, cur_r, cur_c):
    global answer

    if n < 1:
        return

    # 0번째 (제 2사분면)
    if 0 <= cur_r < (2 ** n) / 2 and 0 <= cur_c < (2 ** n) / 2:
        next_r, next_c = cur_r, cur_c
        temp = 0
    # 1번째 (제 1사분면)
    # elif 0 <= cur_r < (2 ** n) / 2 and (2 ** n) / 2 <= cur_c < (2 ** n):
    elif 0 <= cur_r < (2 ** n) / 2 <= cur_c < (2 ** n):
        next_r, next_c = cur_r, cur_c - ((2 ** n) / 2)
        temp = 1
    # 2번째 (제 3사분면)
    elif 0 <= cur_c < (2 ** n) / 2 <= cur_r < (2 ** n):
        next_r, next_c = cur_r - ((2 ** n) / 2), cur_c
        temp = 2
    # 3번째 (제 4사분면)
    elif (2 ** n) / 2 <= cur_r < (2 ** n) and (2 ** n) / 2 <= cur_c < (2 ** n):
        next_r, next_c = cur_r - ((2 ** n) / 2), cur_c - ((2 ** n) / 2)
        temp = 3

    answer += ((2 ** n) / 2 * (2 ** n) / 2 * temp)
    z(n - 1, next_r, next_c)


N, r, c = map(int, input().split())
answer = 0
z(N, r, c)
print(int(answer))
