def solution(numbers, hand):
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    L = mat[3][0]
    R = mat[3][2]
    answer = []
    for i in range(len(numbers)):
        if numbers[i] == 1:
            answer.append('L')
            L = mat[0][0]
            
        elif numbers[i] == 2:
            if R == '#':
                if L in [1,4,5,7,8,0]:
                    answer.append('L')
                    L = mat[0][1]
                else:
                    if hand == 'right':
                        answer.append('R')
                        R = mat[0][1]
                    else:
                        answer.append('L')
                        L = mat[0][1]
            elif L == '*':
                if R in [3,5,6,8,9,0]:
                    answer.append('R')
                    R = mat[0][1]
                else:
                    if hand == 'right':
                        answer.append('R')
                        R = mat[0][1]
                    else:
                        answer.append('L')
                        L = mat[0][1]
            elif R == 0:
                answer.append('L')
                L = mat[0][1]
            elif L == 0:
                answer.append('R')
                R = mat[0][1]
            elif L == 4 and R == 6:
                if hand == 'right':
                    answer.append('R')
                    R = mat[0][1]
                else:
                    answer.append('L')
                    L = mat[0][1]
            elif L == 7 and R == 9:
                if hand == 'right':
                    answer.append('R')
                    R = mat[0][1]
                else:
                    answer.append('L')
                    L = mat[0][1]
            elif abs(L - 2) > abs(R - 2):
                if L == 5 and R == 3:
                    if hand == 'right':
                        answer.append('R')
                        R = mat[0][1]
                    else:
                        answer.append('L')
                        L = mat[0][1]
                else:
                    answer.append('R')
                    R = mat[0][1]
            elif abs(L - 2) < abs(R - 2):
                if L == 4 and R == 5:
                    answer.append('R')
                    R = mat[0][1]
                elif L == 7 and R == 8:
                    answer.append('R')
                    R = mat[0][1]
                else:
                    answer.append('L')
                    L = mat[0][1]
            elif abs(L - 2) == abs(R - 2):
                if hand == 'right':
                    answer.append('R')
                    R = mat[0][1]
                else:
                    answer.append('L')
                    L = mat[0][1]
                
        elif numbers[i] == 3:
            answer.append('R')
            R = mat[0][2]
            
        elif numbers[i] == 4:
            answer.append('L')
            L = mat[1][0]
            
        elif numbers[i] == 5:
            if R == '#':
                if L in [1,4,2,7,8,0]:
                    answer.append('L')
                    L = mat[1][1]
                else:
                    if hand == 'right':
                        answer.append('R')
                        R = mat[1][1]
                    else:
                        answer.append('L')
                        L = mat[1][1]
            elif L == '*':
                if R in [3,2,6,8,9,0]:
                    answer.append('R')
                    R = mat[1][1]
                else:
                    if hand == 'right':
                        answer.append('R')
                        R = mat[1][1]
                    else:
                        answer.append('L')
                        L = mat[1][1]
            elif R == 0:
                answer.append('L')
                L = mat[1][1]
            elif L == 0:
                answer.append('R')
                R = mat[1][1]
            elif L == 1 and R == 3:
                if hand == 'right':
                    answer.append('R')
                    R = mat[1][1]
                else:
                    answer.append('L')
                    L = mat[1][1]
            elif L == 7 and R == 9:
                if hand == 'right':
                    answer.append('R')
                    R = mat[1][1]
                else:
                    answer.append('L')
                    L = mat[1][1]
            elif abs(L - 5) > abs(R - 5):
                if L == 2 and R == 3:
                    answer.append('L')
                    L = mat[1][1]
                else:
                    answer.append('R')
                    R = mat[1][1]
            elif abs(L - 5) < abs(R - 5):
                if L == 7 and R == 8:
                    answer.append('R')
                    R = mat[1][1]
                elif L == 4 and R == 2:
                    if hand == 'right':
                        answer.append('R')
                        R = mat[1][1]
                    else:
                        answer.append('L')
                        L = mat[1][1]
                else:
                    answer.append('L')
                    L = mat[1][1]
            elif abs(L - 5) == abs(R - 5):
                if hand == 'right':
                    answer.append('R')
                    R = mat[1][1]
                else:
                    answer.append('L')
                    L = mat[1][1]
        
        elif numbers[i] == 6:
            answer.append('R')
            R = mat[1][2]
            
        elif numbers[i] == 7:
            answer.append('L')
            L = mat[2][0]
            
        elif numbers[i] == 8:
            if R == '#':
                if L in [1,4,5,7,5,0]:
                    answer.append('L')
                    L = mat[2][1]
                else:
                    if hand == 'right':
                        answer.append('R')
                        R = mat[2][1]
                    else:
                        answer.append('L')
                        L = mat[2][1]
            elif L == '*':
                if R in [3,5,6,5,9,0]:
                    answer.append('R')
                    R = mat[2][1]
                else:
                    if hand == 'right':
                        answer.append('R')
                        R = mat[2][1]
                    else:
                        answer.append('L')
                        L = mat[2][1]
            elif R == 0:
                if hand == 'right':
                    answer.append('R')
                    R = mat[2][1]
                else:
                    if L == 7 or L == 5:
                        answer.append('L')
                        L = mat[2][1]
                    else:
                        answer.append('R')
                        R = mat[2][1]
            elif L == 0:
                if hand == 'left':
                    answer.append('L')
                    L = mat[2][1]
                else:
                    if R == 9 or R == 5:
                        answer.append('R')
                        R = mat[2][1]
                    else:
                        answer.append('L')
                        L = mat[2][1]
            elif L == 4 and R == 6:
                if hand == 'right':
                    answer.append('R')
                    R = mat[2][1]
                else:
                    answer.append('L')
                    L = mat[2][1]
            elif L == 1 and R == 3:
                if hand == 'right':
                    answer.append('R')
                    R = mat[2][1]
                else:
                    answer.append('L')
                    L = mat[2][1]
            elif abs(L - 8) > abs(R - 8):
                if L == 2 and R == 3:
                    answer.append('L')
                    L = mat[2][1]
                elif L == 5 and R == 6:
                    answer.append('L')
                    L = mat[2][1]
                elif L == 5 and R == 9:
                    if hand == 'right':
                        answer.append('R')
                        R = mat[2][1]
                    else:
                        answer.append('L')
                        L = mat[2][1]
                elif L == 7 and R == 5:
                    if hand == 'right':
                        answer.append('R')
                        R = mat[3][1]
                    else:
                        answer.append('L')
                        L = mat[3][1]
                else:
                    answer.append('R')
                    R = mat[2][1]
            elif abs(L - 8) < abs(R - 8):
                answer.append('L')
                L = mat[2][1]
            elif abs(L - 8) == abs(R - 8):
                if hand == 'right':
                    answer.append('R')
                    R = mat[2][1]
                else:
                    answer.append('L')
                    L = mat[2][1]
        
        elif numbers[i] == 9:
            answer.append('R')
            R = mat[2][2]
            
        elif numbers[i] == 0:
            if R == '#':
                if hand == 'right':
                    answer.append('R')
                    R = mat[3][1]
                else:
                    if L == '*' or L == 8:
                        answer.append('L')
                        L = mat[3][1]
                    else:
                        answer.append('R')
                        R = mat[3][1]
            elif L == '*':
                if hand == 'left':
                    answer.append('L')
                    L = mat[3][1]
                else:
                    if R == '#' or R == 7:
                        answer.append('R')
                        R = mat[3][1]
                    else:
                        answer.append('L')
                        L = mat[3][1]
            elif L == 1 and R == 3:
                if hand == 'right':
                    answer.append('R')
                    R = mat[3][1]
                else:
                    answer.append('L')
                    L = mat[3][1]
            elif L == 4 and R == 6:
                if hand == 'right':
                    answer.append('R')
                    R = mat[3][1]
                else:
                    answer.append('L')
                    L = mat[3][1]
            elif L == 7 and R == 9:
                if hand == 'right':
                    answer.append('R')
                    R = mat[3][1]
                else:
                    answer.append('L')
                    L = mat[3][1]
            elif L > R:
                answer.append('L')
                L = mat[3][1]
            elif L < R:
                if L == 2 and R == 3:
                    answer.append('L')
                    L = mat[3][1]
                elif L == 5 and R == 6:
                    answer.append('L')
                    L = mat[3][1]
                elif L == 8 and R == 9:
                    answer.append('L')
                    L = mat[3][1]
    
    string = ''
    for i in answer:
        string += i
    return string