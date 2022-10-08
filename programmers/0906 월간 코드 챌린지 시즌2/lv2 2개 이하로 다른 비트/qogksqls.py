def solution(numbers):
    answer = []
    for number in numbers:
        x = list(bin(number)[2:])  # 2 진수 변환
        len_x = len(x)
        while 1:
            number += 1
            comp = list(bin(number)[2:])  # 비교값

            if len(comp) > len_x:  # 자릿수가 많은 경우
                i, count = 0, 1    # 하나가 다르고 시작하기 때문에 count = 1로 시작
                while i < len_x:
                    if x[i] != comp[i + 1]:
                        count += 1
                    if count > 2:
                        break
                    i += 1
                if count <= 2:
                    answer.append(number)
                    break
            else:                   # 자릿수가 같은 경우
                i, count = 0, 0
                while i < len_x:
                    if x[i] != comp[i]:
                        count += 1
                    if count > 2:  # 2개 이상 다르면 break
                        break
                    i += 1
                if count <= 2:
                    answer.append(number)
                    break
    return answer

solution([2,7])
