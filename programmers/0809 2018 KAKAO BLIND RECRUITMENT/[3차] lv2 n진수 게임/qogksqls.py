def convert(n, num):
    result = ''
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    while num > 0:
        result += numbers[num % n]
        num //= n
        if 0 < num < n:
            result += str(num)
            break
    if not result:
        result = '0'
    return result[::-1]


def solution(n, t, m, p):  # n진법, 미리 구할 숫자 개수, 게임 참가 인원, 튜브 순서
    answer = ''
    num, seq = 0, 0
    while len(answer) < t:
        convert_number = convert(n, num)
        for i in range(len(convert_number)):
            seq += 1
            if seq % m == p % m:
                answer += convert_number[i]
            if len(answer) == t:
                break
        print(convert_number)
        num += 1
    print(answer)
    return answer

solution(16, 16, 2, 2)