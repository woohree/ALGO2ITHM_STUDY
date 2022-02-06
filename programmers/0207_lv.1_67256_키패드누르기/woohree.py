def solution(numbers, hand):
    answer = ''
    location_L = 10
    location_R = 12
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            location_L = number
        elif number in [3, 6, 9]:
            answer += 'R'
            location_R = number

        elif number in [2, 5, 8, 0]:
            if number == 0:
                number = 11
            abs_L = abs(number - location_L)
            abs_R = abs(number - location_R)
            dL = abs_L//3 + abs_L%3
            dR = abs_R//3 + abs_R%3
            if dL > dR:
                answer += 'R'
                location_R = number
            elif dL < dR:
                answer += 'L'
                location_L = number
            elif dL == dR:
                if hand == 'right':
                    answer += 'R'
                    location_R = number
                else:
                    answer += 'L'
                    location_L = number
    return answer