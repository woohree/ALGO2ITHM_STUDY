# 45분
# input() 실패 => pypy로는 성공!
# 백준 참고
import sys
sys.stdin = open('M.txt')


# L 커서를 왼쪽으로 한 칸 옮김
# D 커서를 오른쪽으로 한 칸 옮김
# B 커서 왼쪽에 있는 문자를 삭제
# P $ $ 문자를 커서 왼쪽에 추가
def editor():
    global N
    temp = []

    for _ in range(M):
        edit = sys.stdin.readline().split()

        if edit[0] == 'L' and N:
            temp.append(N.pop())
        elif edit[0] == 'D' and temp:
            N.append(temp.pop())
        elif edit[0] == 'B' and N:
            N.pop()
        elif edit[0] == 'P':
            N.append(edit[1])

    while temp:
        N.append(temp.pop())

    return ''.join(N)


T = int(input())

for tc in range(T):
    N = list(map(str, sys.stdin.readline().rstrip()))
    M = int(input())

    print(editor())
