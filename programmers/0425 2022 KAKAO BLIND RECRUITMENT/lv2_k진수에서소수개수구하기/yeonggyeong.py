import math

def solution(n, k):
    
    def change_number(number, k):
        temp = ''
        while number:
            temp += str(number % k)
            number = number // k
        return temp[::-1]    

    def prime_number(number):
        for i in range(2, int(math.sqrt(number))+1):
            if not number % i:
                return 0
        return 1

    # 입력 받은 수를 k진수로 변환
    number = change_number(n, k)
    prime_lst = number.split('0')
    answer = 0
    for i in prime_lst:
        # 1은 소수가 아니고 ''가 아닐때
        if i not in ['1', '']:
            answer += prime_number(int(i))

    return answer

n = 110011
k = 10

print(solution(n, k))