# 90분

# 원판 n개를 옮길 시,
# 탑1에서 n-1개를 탑2에 옮기고,
# 탑1에서 가장 무거운 원판을 탑3에 옮기고,
# 탑2에서 n-1개를 다시 탑3에 옮긴다.
# 라는 아이디어!

# 원판 갯수, 출발탑, 중간탑(관계없는 탑), 도착탑
def hanoi(number, tower1, tower2, tower3):
    # 원판이 하나남으면,
    # 재귀종료
    if number == 1:
        print(f'{tower1} {tower3}')
        return
    # 탑1에서 원판 n-1개를 탑2로 옮김 (원판 묶음)
    hanoi(number-1, tower1, tower3, tower2)
    # 탑1에 남은 가장 무거운 원판을 탑3로 옮김 (원판 1개)
    print(f'{tower1} {tower3}')
    # 탑2에서 원판 n-1개를 탑3에 옮김 (원판 묶음)
    hanoi(number-1, tower2, tower1, tower3)

N = int(input())
# N이 20 이하인 경우,
if N <= 20:
    # f(n) = 2*f(n-1) + 1
    # 1, 3, 7, 15, ... => 2**N - 1
    print(2**N-1)
    hanoi(N, 1, 2, 3)
# N이 20초과인 경우,
else:
    print(2**N-1)