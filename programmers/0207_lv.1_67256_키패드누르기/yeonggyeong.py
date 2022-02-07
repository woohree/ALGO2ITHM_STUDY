def solution(numbers, hand):
    answer = ''
    left_hand = 10 # -1
    right_hand = 12 # 10
    
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left_hand = number
        elif number in [3, 6, 9]:
            answer += 'R'
            right_hand = number
        else :
            number = 11 if number == 0 else number
            
            left_dist = abs(number-left_hand)
            right_dist = abs(number-right_hand)
            
            if (left_dist // 3 + left_dist % 3) < (right_dist // 3 + right_dist % 3) :
                answer += 'L'
                left_hand = number
            elif (left_dist // 3 + left_dist % 3) > (right_dist // 3 + right_dist % 3):
                answer += 'R'
                right_hand = number
            elif (left_dist // 3 + left_dist % 3) == (right_dist // 3 + right_dist % 3):
                if hand == 'left':
                    answer += 'L'
                    left_hand = number 
                else :
                    answer += 'R'
                    right_hand = number
                
    return answer