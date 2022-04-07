import sys
sys.stdin = open('M.txt')


def permutation(n):
    result = 1
    for j in range(n, 0, -1):
        result *= j

    return result


def combination(n, r):
    result = permutation(n) / (permutation(r) * permutation(n - r))

    return result


T = int(input())

for tc in range(T):
    N, M, K = map(int, input().split())

    # 1부터 N까지의 수에서 M개의 서로 다른 수를 고를 경우의 수 NCM
    num_of_cases = combination(N, M)

    # 적어도 K개의 수가 같은 경우의 수 MCK * (N-M)C(M-K)~ MCM * (N-M)C0
    k_cases = 0

    for i in range(K, M + 1):
        if N - M >= M - i:
            k_cases += combination(M, i) * combination(N - M, M - i)

    print(k_cases / num_of_cases)
