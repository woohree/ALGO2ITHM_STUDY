import sys
sys.stdin = open('B.txt')

'''
100분
1. KMP 알고리즘 사용
2. 문자열 비교하면서 P[0]와 같은 알파벳 나오면 plus_index에 저장하고 나중에 i에 더해줌.
3. 근데...
'''

S = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()

len_S, len_P = len(S), len(P)
i = 0
while i <= len_S - len_P:
    plus_index = 1
    if S[i] == P[0]:
        flag = 1
        for j in range(1, len_P):
            if S[i + j] == P[0] and i + j + len_P <= len_S:
                plus_index = j
            if S[i+j] != P[j]:
                flag = 0
                if S[i+j] not in P:
                    plus_index = j + 1
                break
        if flag:
            print(1)
            exit()
    i += plus_index
print(0)

'''
S = input()
P = input()
if P in S:
    print(1)
else:
    print(0)
'''
