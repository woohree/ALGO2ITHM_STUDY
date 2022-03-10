import sys
sys.stdin = open('L.txt')

def make_triangle(N):
    # N이하 사면체 내 삼각형 수
    # ex) N = 11 => total = [1, 4, 10]
    i = 1
    while N >= total[-1]:
        i += 1
        total.append(total[-1] + i*(i+1)//2)
    total.pop()


# 중복을 허용하는 DFS
# total 리스트 내 요소들을 더해(중복허용) N을 만들고, 그 요소 수의 최솟값을 구하는 문제
def get_min_number(i):
    global N, cnt, min_cnt

    for j in range(i, -1, -1):
        if N - total[j] == 0:       # N을 완성한 경우, cnt가 최솟값일 때 min_cnt 갱신
            cnt += 1
            if cnt < min_cnt:
                min_cnt = cnt
            cnt -= 1
        elif N - total[j] > 0:      # 아직 N을 완성하지 못한 경우,
            if cnt < min_cnt-2:     # 가지치기
                N -= total[j]
                cnt += 1
                get_min_number(j)   # j를 인자로 재귀!
                N += total[j]       # 다시 돌아왔을 때, 변한 N, cnt 값을 원상복구
                cnt -= 1
            else:                   # 가지치기
                break


N = int(sys.stdin.readline().rstrip())
cnt = 0
min_cnt = N                         # min_cnt의 초기 값, N보다 커질 수 없다.
total = [1]
make_triangle(N)
get_min_number(len(total)-1)
print(min_cnt)
