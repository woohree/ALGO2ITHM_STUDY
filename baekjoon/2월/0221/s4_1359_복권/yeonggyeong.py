import sys
sys.stdin = open('G.txt')


n, m, k = map(int, input().split())

# factorial 연산 구현
def fact(x):
    factorial = 1
    for i in range(1, x+1):
        factorial *= i
    return factorial

# combination 연산 구현
def C(n, m):
    return int(fact(n)/(fact(m)*fact(n-m)))

# k가 m보다 작을때까지 반복, k가 같을때, k + 1개가 같을 때 모두 반복하여 결과에 더해주기
result =0
for i in range(k,m+1):
    result += C(m, i) * C(n-m , m-i)
    
answer = round(result / C(n, m), 9)
print(answer)
