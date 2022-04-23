

# 40분
def get_real_numbers(n, k, n_list):
    temp = divmod(n, k)                     # (몫, 나머지) 반환
    n_list.append(temp[1])                  # 나머지는 인자에 추가

    if not temp[0]:                         # 몫이 0이라면, 진수변환 완료!
        result = []
        stack = []
        for number in n_list:
            if not number:                  # 0일때,
                if stack and stack != [1]:  # 스택이 존재하고, 1이 아니라면, result에 거꾸로 추가!
                    result.append(int(''.join(map(str, stack[::-1]))))
                stack = []
            else:
                stack.append(number)        # 그 외, 스택에 추가!

        if stack:                           # 다했는데 남았으면, result에 거꾸로 추가!
            result.append(int(''.join(map(str, stack[::-1]))))

        return result

    else:                                   # 몫이 0이 아니라면, 재귀!
        return get_real_numbers(temp[0], k, n_list)


def solution(n, k):
    answer = 0
    numbers = get_real_numbers(n, k, [])    # 진수 변환하고, 0에서 끊은 수 리스트
    for number in numbers:
        if number == 2:                     # 2는 소수
            answer += 1
            continue

        if number != 1 and number % 2:      # 1이 아니고, 홀수일 때,
            for i in range(3, int(number**(1/2)), 2):
                if not number % i:          # 나누어 떨어지면, 소수가 아님!
                    break
            else:                           # 소수면 추가!
                answer += 1
    return answer


n = 10
k = 10
print(solution(n, k))
# print(n**(1/2))