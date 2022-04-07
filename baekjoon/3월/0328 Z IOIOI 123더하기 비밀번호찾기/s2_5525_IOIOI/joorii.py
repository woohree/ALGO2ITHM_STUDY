import sys
sys.stdin = open('M.txt')


def get_count():
    cnt = answer = idx = 0
    while idx < M - 2:
        if S[idx:idx + 3] == 'IOI':
            cnt += 1
            idx += 2
        else:
            cnt = 0
            idx += 1

        if cnt == N:
            cnt -= 1
            answer += 1

    return answer


N = int(input())
M = int(input())
S = input()

print(get_count())

"""
# 50점
def get_p(n):
    string = 'I'
    for _ in range(n):
        string += 'OI'
    return string


def get_count(p):
    cnt = 0
    p_len = len(p)
    for i in range(M - p_len + 1):
        if S[i:i + p_len] == p:
            cnt += 1
    return cnt


N = int(input())
M = int(input())
S = input()

print(get_count(get_p(N)))
"""