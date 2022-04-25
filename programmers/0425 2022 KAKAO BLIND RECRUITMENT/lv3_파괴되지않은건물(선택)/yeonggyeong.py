
board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

# 스킬 [type(1->적, 2-> 아군), r1, c1, r2, c2, degree]
def solution(board, skill):

    for s in skill:
        skill_type = s[0]
        r1, c1, r2, c2 = s[1:5]
        degree = s[5]

        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                if skill_type == 1:
                    board[r][c] -= degree
                else:
                    board[r][c] += degree
    answer = 0
    for row in board:
        for col in row:
            if col > 0:
                answer += 1
    return answer
print(solution(board, skill))