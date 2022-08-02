import sys
sys.stdin = open('input.txt')

tc = int(input())
for _ in range(tc):
    N = int(input())
    R = list(map(int, input().split()))
    isImpossible = 0
    # R[i]가 있을 때 S[i-1]까지 S[i]보다 작은 수의 갯수==R[i]
    make = []
    for i in range(len(R)):
        # i번째까지 크기가 작은 게 없다면 제일 작은 수를 줌
        if R[i] == 0:
            make.append(N-i)
        # 지금까지 가질 수 있는 갯수보다 작은 수의 갯수가 더 크다면,
        # 잘못된 것임
        elif R[i] > i:
            isImpossible = 1
            break
        # 가질 수 있는 작거나 같으면서 숫자를 가지면
        # 순위에 변동이 옴.
        # S[i]는 지금까지 가질 수 있었던 숫자(N-i)
        # 에서 N-i+R[i]한 값을 가져야함.
        elif R[i] <= i and R[i] != 0:
            for j in range(len(make)):
                if make[j] <= N-i+R[i]:
                    make[j] -= 1
            make.append(N-i+R[i])
    if isImpossible != 0:
        print('IMPOSSIBLE')
    else:
        print(*make)

