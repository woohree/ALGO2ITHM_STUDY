def solution(dartResult):
    result = []
    i = 0
    while i < len(dartResult):
        if dartResult[i].isdigit():
            num = dartResult[i]
            j = i + 1
            while j < len(dartResult):  # 숫자 2자리 수 넘는거 검사
                if dartResult[j].isdigit():
                    num += dartResult[j]
                    j += 1
                else:
                    i = j - 1
                    break
            result.append(int(num))
        elif dartResult[i].isalpha():
            if dartResult[i] == 'D':
                result[-1] **= 2
            elif dartResult[i] == 'T':
                result[-1] **= 3
        else:
            if dartResult[i] == '*':
                result[-1] *= 2
                if len(result) >= 2:  # 전 값 2배
                    result[-2] *= 2
            elif dartResult[i] == '#':
                result[-1] *= -1
        i += 1
    answer = sum(result)
    return answer