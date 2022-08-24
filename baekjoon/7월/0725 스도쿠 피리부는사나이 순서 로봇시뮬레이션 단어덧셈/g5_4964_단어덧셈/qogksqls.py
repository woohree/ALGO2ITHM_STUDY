import sys
sys.stdin = open('B.txt')


def dfs():

    return


while 1:
    N = int(input())
    if N == 0:
        break
    left = []
    alphabets = {}
    for n in range(N):
        alpha = input()
        for i in range(len(list(alpha))):
            if i == 0:
                if not alphabets.get(alpha[0]):
                    alphabets[alpha[0]] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            else:
                if not alphabets.get(alpha[i]):
                    alphabets[alpha[i]] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if n != N-1:
            left.append(alpha)
        else:
            right = alpha
    dfs()
