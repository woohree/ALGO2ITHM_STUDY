import sys
sys.stdin = open('G.txt')

def editor():
    string = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    commands = [list(sys.stdin.readline().rstrip().split()) for _ in range(n)]

    # 커서의 왼쪽 문자
    left = list(string)
    # 커서의 오른쪽 문자
    right = []

    for command in commands:
        # 명령이 L이고 커서 왼쪽 문자가 있다면 커서 왼쪽 문자의 마지막을 커서 오른쪽으로 추가
        if command[0] == 'L' and left:
            right.append(left.pop())
        # 명령이 D이고 커서 오른쪽 문자가 있다면 커서 오른쪽 문자의 마지막을 커서 왼쪽으로 추가
        elif command[0] == 'D' and right:
            left.append(right.pop(-1))
        # 명령이 B이고 왼쪽 문자가 있다면 커서 왼쪽 문자의 마지막 제거
        elif command[0] == 'B' and left:
            left.pop()
        # 명령이 P라면 커서 왼쪽에 해당 문자열 추가
        elif command[0] == 'P':
            left.append(command[1])
        else:
            continue
        
    # 왼쪽과 오른쪽 합
    result = left + right[::-1]
    return ''.join(result)

answer = editor()
print(answer)