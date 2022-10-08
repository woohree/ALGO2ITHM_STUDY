import sys
sys.stdin = open('W.txt')


T = int(input())
for _ in range(T):
    n = int(input())
    R = list(map(int, input().split()))
    visited = [i for i in range(1, n+1)]    # 넣을 숫자
    S = []
    for i in range(n-1, -1, -1):            # 거꾸로 읽기
        if len(visited) <= R[i]:            # 넣을 숫자 배열 길이가 R[i]보다 작으면, 더이상 넣을 수가 없음
            print('IMPOSSIBLE')
            break
        S.append(visited.pop(R[i]))         # visited에서 R[i] 인덱스를 찾아 pop시키고 그 값을 S에 넣는다
    else:
        for s in S[::-1]:                   # 뒤에서부터 push했으니, 거꾸로 출력
            print(s, end=' ')
        print()