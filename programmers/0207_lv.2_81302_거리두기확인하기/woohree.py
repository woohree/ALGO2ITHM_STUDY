def solution(places):  # 1시간, 포기
    answer = []
    # p기준, 가로세로로 1칸 안에 p가 없어야함
    # o기준, 가로세로로 1칸 안에 p가 1개 이하
    for idx in range(len(places)):
        for i in range(len(places[idx])):
            for j in range(len(places[idx][0])):
                if places[idx][i][j] == 'P':
                    if places[idx][i+1][j] == 'P' or places[idx][i][j+1] == 'P':
                        answer.append(0)
                elif places[idx][i][j] == 'O':
                    if bool(places[idx][i+1][j] == 'P') + (bool(places[idx][i][j+1] == 'P')) >= 1:
                        answer.append(0)
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
# [1, 0, 1, 1, 1]

