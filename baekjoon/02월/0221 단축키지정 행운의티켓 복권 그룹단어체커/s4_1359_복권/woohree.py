import sys
sys.stdin = open('L.txt')

# 80분

# 팩토리얼 구현
def factorial(number):
    result = 1
    for n in range(1, number+1):
        result *= n
    return result

# 조합(콤비네이션) 구현
def combination(number1, number2):
    result = factorial(number1) / (factorial(number2) * factorial(number1-number2))
    return result


data = list(map(int, input().split()))
N, M, K = data[0], data[1], data[2]

# 적어도 k개 이상일 때 당첨이므로, k부터 M까지의 확률을 다 더해줘야 함
ans = 0
for k in range(K, M+1):
    # N-M 보다 M-k가 큰 경우, 확률은 그냥 100%
    if N-M < M-k:
        ans = 1.0
        break
    ans += combination(M, k) * combination(N-M, M-k) / combination(N, M)

print(ans)
