# 영어 소문자만을 기록할 수 있는 편집기, 최대 600,000글자까지 입력
# L 	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
# D 	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
# B 	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
#       삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
# P $  	$라는 문자를 커서 왼쪽에 추가함

# 45분

import sys
sys.stdin = open('B.txt')

# input() 대신 sys.stdin.readline()을 써야하는 순간같다.
# 하지만 '\n'이 마지막에 들어오는 것만 pop으로 빼주면 된다.
strings = list(sys.stdin.readline())
strings.pop()

N = len(strings)
M = int(sys.stdin.readline())
orders = [list(sys.stdin.readline().split()) for _ in range(M)]

# 예전 우현님이 하셨던 방식. 요긴하게 사용했다.
temp = []
for order in orders:
    # N이 0보다 커야하는 조건을 넣어 줌으로써, 커서가 왼쪽으로 계속 가는 것을 방지
    if N > 0 and order[0] == 'L':
        temp.append(strings.pop())
        N -= 1
    # temp가 0일 때는 오른쪽으로 갈 수 없다는 조건을 넣어 줌으로써, 커서가 오른쪽으로 계속 가는 것을 방지
    elif len(temp) != 0 and order[0] == 'D':
        strings.append(temp.pop())
        N += 1
    # N이 0보다 커야하는 조건을 넣어 줌으로써, 문자열이 비었을 때 지우는 것을 방지
    elif N > 0 and order[0] == 'B':
        strings.pop()
        N -= 1
    # P는 추가만 하는 거라 따로 조건 안 넣어도 된다.
    elif order[0] == 'P':
        strings.append(order[1])
        N += 1

# temp에 있는 문자들을 뒤에서부터 다시 strings에 집어 넣음
for _ in range(len(temp)):
    strings.append(temp.pop())

print(''.join(strings))
