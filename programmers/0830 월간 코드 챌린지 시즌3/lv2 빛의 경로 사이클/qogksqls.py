'''
1. 모든 점으로부터 4방향 검사
2. memories에 현재 점 위치와 다음 점 위치 저장
3. not in memories 로 겹치는 이동이 발견되면 while문 종료 후 count가 0이 아니라면 answer에 저장
'''


def solution(grid):
    answer = []
    moves = ((0, 1), (1, 0), (0, -1), (-1, 0))
    memories = set()
    row, col = len(grid), len(grid[0])
    for x in range(row):  # 1번
        for y in range(col):
            for move in moves:
                now = (x, y)
                d = move
                count = 0
                nxt = (x, y, d)
                if now[0] + d[0] == -1:
                    now = (row - 1, now[1])
                elif now[0] + d[0] == row:
                    now = (0, now[1])
                elif now[1] + d[1] == -1:
                    now = (now[0], col - 1)
                elif now[1] + d[1] == col:
                    now = (now[0], 0)
                else:
                    now = (now[0]+d[0], now[1]+d[1])
                while nxt not in memories:  # 3번
                    memories.add(nxt)  # 2번
                    # print(nxt)
                    if grid[now[0]][now[1]] == 'R':
                        if d == (0, 1):
                            d = (1, 0)
                        elif d == (1, 0):
                            d = (0, -1)
                        elif d == (0, -1):
                            d = (-1, 0)
                        elif d == (-1, 0):
                            d = (0, 1)
                    elif grid[now[0]][now[1]] == 'L':
                        if d == (0, 1):
                            d = (-1, 0)
                        elif d == (1, 0):
                            d = (0, 1)
                        elif d == (0, -1):
                            d = (1, 0)
                        elif d == (-1, 0):
                            d = (0, -1)

                    nxt = (now[0], now[1], d)
                    if now[0] + d[0] == -1:
                        now = (row - 1, now[1])
                    elif now[0] + d[0] == row:
                        now = (0, now[1])
                    elif now[1] + d[1] == -1:
                        now = (now[0], col - 1)
                    elif now[1] + d[1] == col:
                        now = (now[0], 0)
                    else:
                        now = (now[0]+d[0], now[1]+d[1])
                    count += 1
                if count: answer.append(count)  # answer
    answer.sort()
    print(answer)
    return answer


solution(["SL", "LR"])
