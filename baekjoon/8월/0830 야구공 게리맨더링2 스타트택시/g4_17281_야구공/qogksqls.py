import sys
from itertools import permutations
sys.stdin = open('B.txt')

'''
1. 문제 이해하는데 오래걸리고, 시간초과 늪에 빠졌다.
2. 순열까지는 괜찮은데 나는 주자들이 도는걸 stack or queue로 하는 바람에 시간초과가 걸렸다.
3. 결국 구글링하니까 단순하게 하는 걸 보고 고치니 구글링 코드랑 거의 비슷해졌지만 pass함.
4. 개빡친다.
'''

N = int(sys.stdin.readline().rstrip())
innings = [list(map(int, input().split())) for _ in range(N)]

perm = list(permutations([1, 2, 3, 4, 5, 6, 7, 8], 8))
max_score = 0
for p in perm:  # 순열 돌리기
    idx = list(p[:3]) + [0] + list(p[3:])
    j, score = 0, 0
    for i in range(N):  # 한 이닝 진행
        out = 0
        base1, base2, base3 = 0, 0, 0
        while out != 3:
            temp = 0
            if innings[i][idx[j]] == 0:
                out += 1
            elif innings[i][idx[j]] == 1:
                score += base3
                base1, base2, base3 = 1, base1, base2
            elif innings[i][idx[j]] == 2:
                score += base2 + base3
                base1, base2, base3 = 0, 1, base1
            elif innings[i][idx[j]] == 3:
                score += base1 + base2 + base3
                base1, base2, base3 = 0, 0, 1
            elif innings[i][idx[j]] == 4:
                score += base1 + base2 + base3 + 1
                base1, base2, base3 = 0, 0, 0
            j += 1
            if j == 9:
                j = 0
    max_score = max(max_score, score)
print(max_score)
