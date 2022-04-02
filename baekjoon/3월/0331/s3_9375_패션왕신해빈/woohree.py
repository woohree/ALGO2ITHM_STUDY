import sys
sys.stdin = open('L.txt')


"""
중복 순열 구하는 문제
- 각 옷의 종류가 몇개 나왔는지 세서 중복순열 계산

예시) 모자를 안 쓰는 경우(0), hat을 쓰는 경우(1), turban을 쓰는 경우(2), 3가지
     안경을 안 쓰는 경우(0), sunglass를 쓰는 경우(1), 2가지
     이때, 중복순열을 구하면 2x3 = 6
     하지만 아무것도 안 입는 경우는 없으므로, 6 - 1 = 5
"""


T = int(sys.stdin.readline().rstrip())
for tc in range(1, T+1):
    N = int(sys.stdin.readline().rstrip())

    check = {}
    for _ in range(N):
        x = sys.stdin.readline().rstrip().split()
        check.setdefault(x[1], 1)                   # 디폴트 값은 1(안 입는 경우)
        check[x[1]] += 1

    ans = 1
    for key in check:
        ans *= check[key]
    print(ans-1)
