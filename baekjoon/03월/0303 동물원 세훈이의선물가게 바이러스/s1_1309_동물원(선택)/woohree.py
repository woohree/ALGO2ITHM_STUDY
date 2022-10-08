import sys
sys.stdin = open('L.txt')


# x x / x o / o x - 세 가지 경우로 나누어 생각
# 1. x x
#    다음 줄에 x x / x o / o x 가능
# 2. x o
#    다음 줄에 x x / o x 가능
# 3. o x
#    다음 줄에 x x / x o 가능
def get_array_of_rions(N):
    if N == 1:
        return 3
    # 리스트를 N 만큼 뽑아놓고 했었는데, 메모리 초과가 떠서 바꿈
    # 마지막 단에 [:]때문에 시간이 조금 오래 걸리나 잘 모르겠음
    # x x, x o, o x 각각 다음으로 올 수 있는 경우의 수
    cnt = [[3, 2, 2]] + [[0]*3]
    n = 2
    while n < N:
        n += 1
        cnt[1][0] = cnt[0][0] + cnt[0][1] + cnt[0][2]  # x x
        cnt[1][1] = cnt[0][0] + cnt[0][2]              # x o
        cnt[1][2] = cnt[0][0] + cnt[0][1]              # o x
        cnt[0] = cnt[1][:]                             # 약간(?) 깊은 복사

    return sum(cnt[0])


N = int(input())
ans = get_array_of_rions(N)
print(ans%9901)