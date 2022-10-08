# import sys
# sys.stdin = open('G.txt')

# n = int(input())
# commands = [list(input().split()) for _ in range(n)]
# commands = { time:[t,s] for t, s, time in commands}

# dic = { '0' : ''}
# for t in range(1, int(list(commands.keys())[-1])+1):
#     if commands.get(str(t)):
#         command = commands.get(str(t))
#         if command[0] == 'type':
#             dic[str(t)] = dic[str(t-1)] + command[1]
#         else:
#             re = t - int(command[1]) - 1
#             dic[str(t)] = dic[str(re)]
#     else:
#         dic[str(t)] = dic[str(t-1)]

# print(list(dic.values())[-1])

import sys
sys.stdin = open('G.txt')

n = int(sys.stdin.readline())

results = [(0, '')]
for i in range(n):
    t, s, time = sys.stdin.readline().rstrip().split()
    # type일때는 그 전의 값에 문자열 더해주기
    if t == 'type':
        results.append((int(time), results[-1][1] + s))
    else:
        # 되돌아가야하는 시간
        re = int(time) - int(s) - 1
        # 시간이 0이하일때는 빈 문자열
        if re <= 0:
            results.append((int(time), ''))
        # 되돌아가야하는 시간으로 돌아가기
        for j in range(len(results)-1, -1, -1):
            if results[j][0] <= re:
                results.append((int(time), results[j][1]))
                break
print(results[-1][-1])

            