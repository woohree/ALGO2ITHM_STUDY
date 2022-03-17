import sys
sys.stdin = open('L.txt')


def get_maximum_profit():
    for i in range(N-1, -1, -1):    # 앞부터 보면, 스케쥴을 조금 가공해야 해서 뒤부터 봄
        if i + schedule[i][0] > N:  # 상담 종료일이 퇴사일을 지나는 경우,
            dp[i] = dp[i+1]         # 가장 최근까지의 이익과 같음
        else:                                                           # 그 외,
            dp[i] = max(schedule[i][1]+dp[i+schedule[i][0]], dp[i+1])   # 상당 종료일 이전(뒤부터니까 이후?)의 이득+당일 / 최근까지의 이익 중, 큰 값을 택함


N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]  # 뒤부터 봐야 하니까, N+1 길이만큼 만들어 둚
get_maximum_profit()
print(dp.pop(0))


# 아 삽질이여
# def get_maximum_profit_in(days):
#     idx = 0
#     for day in days:
#         if not dp:
#             if day:
#                 dp.append([idx, day[0][1][1]])
#             else:
#                 dp.append([idx, 0])
#         elif day:
#             max_d = 0
#             max_d_idx = 0
#             idx2 = 0
#             for d in day:
#                 if d[0] <= dp[-1][0] and d[1][1] > max_d_idx:
#                     max_d_idx, idx2 = d[1][1], d[0]
#                 elif d[0] > dp[-1][0] and d[1][1] > max_d:
#                     max_d = d[1][1]
#             if not idx2 and max_d+dp[-1][1] > max_d_idx:
#                 dp.append([idx, max_d+dp[-1][1]])
#             elif not max_d_idx or max_d+dp[-1][1] > max_d_idx+dp[idx2-1][1]:
#                 dp.append([idx, max_d+dp[-1][1]])
#             else:
#                 if idx2 == 0:
#                     dp.append([idx, max_d_idx])
#                 else:
#                     dp.append([idx, max_d_idx+dp[idx2-1][1]])
#         else:
#             dp.append([dp[-1][0], dp[-1][1]])
#         idx += 1
#     return dp[-1][1]
# 
# 
# N = int(input())
# days = [[] for _ in range(N)]
# schedules = [list(map(int, input().split())) for _ in range(N)]
# idx = 0
# for schedule in schedules:
#     if schedule[0]+idx-1 < N:
#         days[schedule[0]+idx-1].append([idx, schedule])
#     idx += 1
# dp = []
# # print(days)
# ans = get_maximum_profit_in(days)
# print(ans)

