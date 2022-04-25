import math

'''
1. 10진수 정수 n을 k진수로 변환한 convert_k 라는 list 로 저장
2. 0을 기준으로 0이 아닌 숫자들을 numbers list 에 저장
3. 소수를 찾는 함수를 만들어 numbers에 저장된 숫자가 소수인지 검사 후 count
'''


# k진수 변환
def convert(n, k):
    numbers = []
    while 1:
        numbers.append(n % k)
        n //= k
        if n < k:
            numbers.append(n)
            numbers = numbers[::-1]
            return numbers


# 소수 찾기
def is_prime_number(x):
    '''
    for i in range(2, x or x // 2 + 1):
        if x % i == 0:
            return False
    return True
    '''
    # 16을 예로 들면,
    # 1, 2, 4, 8, 16 -> 16의 소수들
    # 4를 기준으로 왼쪽을 검사하면 오른쪽은 검사할 필요가 없다.
    # 따라서 범위를 (제곱근 + 1)까지로 설정
    for i in range(2, int(math.sqrt(x)) + 1):  # int() -> 정수 부분만 가져옴
        if x % i == 0:
            return False
    return True

n = 437674
k = 3

# k진수로 변환
convert_k = convert(n, k)

# 리스트로 나열된 convert_k를 str형식으로 numbers에 저장
numbers = []
temp = ''
for number in convert_k:
    if number == 0:
        numbers.append(temp)
        temp = ''
    else:
        temp += str(number)
# 리스트의 마지막이 0으로 끝나지 않은 경우로, for 문 이후 temp가 False 값이 아니라면 한 번 더 append 해줘야 한다.
if temp:
    numbers.append(temp)

# 소수 찾기
answer = 0
for number in numbers:
    # number가 False가 아닌지 검사
    if number:
        number = int(number)  # int형으로 바꿔주고
        # 1보다 큰 숫자만 봐야하므로
        if number > 1:
            if is_prime_number(number):
                answer += 1

print(answer)
