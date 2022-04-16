import sys
sys.stdin = open('L.txt')


def shoot(fireballs):
    moves = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))  # 이동방향(d)에 맞춤
    for _ in range(K):
        temp = {}                               # 겹치는 애들 확인할 딕셔너리
        news = []                               # 이동 끝난 파이어볼들
        for i in range(len(fireballs)):
            r, c, m, s, d = fireballs[i]
            if s and m:                         # 속도, 질량이 0보다 커야함
                fireballs[i][0] += moves[d][0]*s
                while fireballs[i][0] < 1:      # 인덱스 벗어나는거 작업
                    fireballs[i][0] = N+fireballs[i][0]
                while fireballs[i][0] > N:
                    fireballs[i][0] = fireballs[i][0]-N

                fireballs[i][1] += moves[d][1]*s
                while fireballs[i][1] < 1:      # 인덱스 벗어나는거 작업
                    fireballs[i][1] = N+fireballs[i][1]
                while fireballs[i][1] > N:
                    fireballs[i][1] = fireballs[i][1]-N

                new_r, new_c = fireballs[i][0], fireballs[i][1]
                if temp.get((new_r, new_c)):    # 겹치면, append
                    temp[(new_r, new_c)].append([new_r, new_c, m, s, d])
                else:                           # 처음이면, 키 추가
                    temp[(new_r, new_c)] = [[new_r, new_c, m, s, d]]

        for key in temp:                        # 겹치는 애들 처리 작업
            if len(temp[key]) > 1:
                new_m = new_s = d_flag_odd = d_flag_even = 0
                for i in range(len(temp[key])):
                    new_m += temp[key][i][2]    # 질량, 속도 총합 구하기
                    new_s += temp[key][i][3]
                    if temp[key][i][4] % 2:     # 방향 홀, 짝 체크
                        d_flag_odd += 1
                    else:
                        d_flag_even += 1
                if d_flag_odd == len(temp[key]) or d_flag_even == len(temp[key]):
                    new_d = (0, 2, 4, 6)        # 전부 홀or짝일 경우,
                else:
                    new_d = (1, 3, 5, 7)        # 아닐 경우,

                for i in range(4):              # 겹치는 애들 작업한 뒤, 새로 파이어볼 4개 만들기
                    if new_m // 5:
                        news.append([key[0], key[1], new_m//5, new_s//len(temp[key]), new_d[i]])
            else:                               # 안 겹치는 애들은 그대로 추가
                news.append(temp[key][0])
        fireballs = news                        # 파이어볼들 갱신
    return fireballs


N, M, K = map(int, sys.stdin.readline().split())
fireballs = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
result = shoot(fireballs)
ans = 0
for i in range(len(result)):
    ans_m, ans_s = result[i][2], result[i][3]
    if ans_s and ans_m:
        ans += ans_m
print(ans)
