import sys
sys.stdin = open('L.txt')


def drink(wines):
    if n == 1:
        return wines[1]
    elif n == 2:
        return wines[1] + wines[2]
    else:
        dp.append(0)                    # 안 마신 효주
        dp.append(wines[1])             # 1잔 마신 효주
        dp.append(wines[1]+wines[2])    # 2잔 마신 효주
        for i in range(3, n+1):
            dp.append(max(dp[i-3]+wines[i-1]+wines[i], dp[i-2]+wines[i], dp[i-1]))  # 3잔 이상 연속으로 마시기 불가능,
        return dp[-1]             # 따라서, 3잔 전까지 + 최근 두잔 / 2잔 전까지 + 최근 한잔 / 1잔 전까지, 중 최대값을 찾는다.


n = int(sys.stdin.readline().rstrip())
wines = [0] + [int(sys.stdin.readline().rstrip()) for _ in range(n)]  # 인덱스 맞추려고 앞에 0 추가
dp = []
ans = drink(wines)
print(ans)

# 삽질한 자국
# def drink(i):
#     global a, max_a
#     if i == n:
#         if a > max_a:
#             max_a = a
#     else:
#         for _ in range(2):
#             if i == 0:
#                 if not bool_wines[i]:
#                     bool_wines[i] = True
#                     a += wines[i]
#                     drink(i+1)
#                     a -= wines[i]
#                 else:
#                     bool_wines[i] = False
#                     drink(i+1)
#             elif i == n-1:
#                 if not bool_wines[i-1]:
#                     bool_wines[i] = True
#                     a += wines[i]
#                     drink(i + 1)
#                     a -= wines[i]
#                 elif bool_wines[i-1]:
#                     if bool_wines[i-2]:
#                         bool_wines[i] = False
#                         drink(i+1)
#                     elif not bool_wines[i-2]:
#                         bool_wines[i] = True
#                         a += wines[i]
#                         drink(i+1)
#                         a -= wines[i]
#                 break
#
#             elif not bool_wines[i-1]:
#                 bool_wines[i] = True
#                 a += wines[i]
#                 drink(i+1)
#                 a -= wines[i]
#                 break
#             elif bool_wines[i-1]:
#                 if i == 1:
#                     if not bool_wines[i]:
#                         bool_wines[i] = True
#                         a += wines[i]
#                         drink(i+1)
#                         a -= wines[i]
#                     else:
#                         bool_wines[i] = False
#                         drink(i+1)
#                 elif bool_wines[i-2]:
#                     bool_wines[i] = False
#                     drink(i+1)
#                     break
#                 elif not bool_wines[i-2]:
#                     bool_wines[i] = True
#                     a += wines[i]
#                     drink(i+1)
#                     a -= wines[i]
#
#
# n = int(sys.stdin.readline().rstrip())
# wines = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
# bool_wines = [False] * n
# a = 0
# max_a = 0
# drink(0)
# print(max_a)
