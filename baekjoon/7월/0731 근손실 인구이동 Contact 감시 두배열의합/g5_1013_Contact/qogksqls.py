import sys
sys.stdin = open('B.txt')

'''
(100+1+ | 01)+

'''


def dfs(s):
    global flag
    if s == len_sign:
        flag = 1
        return
    if sign[s:s+3] == '100':
        s += 3
        if s == len_sign:
            return
        while sign[s] == '0':
            s += 1
            if s == len_sign:
                return
        while sign[s] == '1':
            s += 1
            if s == len_sign:
                flag = 1
                return
        if sign[s-2] == '1':
            for i in range(2):
                dfs(s - i)
        else:
            dfs(s)
    elif sign[s] == '0':
        if s + 1 < len_sign and sign[s + 1] == '1':
            dfs(s + 2)
        else:
            return
    return


T = int(input())
for _ in range(T):
    sign = input()
    len_sign = len(list(sign))
    flag = 0
    dfs(0)
    if flag:
        print('YES')
    else:
        print('NO')
