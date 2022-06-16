import sys
sys.stdin = open('L.txt')


def write(lines):
    real = ''                               # 현재까지 문자열
    temp = []                               # 문자열, 시간 저장
    for line in lines:
        command, char, t = line[0], line[1], int(line[2])
        if command == 'type':
            real += char
            temp.append((real, t))
        else:                               # undo
            char = int(char)
            for i in range(len(temp)-1, -1, -1):
                if temp[i][1] < t - char:   # undo하는 시간 바로 직전
                    real = temp[i][0]       # 그 순간으로 real 갱신
                    temp.append((real, t))  # 저장소도 갱신
                    break
            else:
                real = ''                   # 만약, 끝까지 문제가 없으면 문자열 초기화
                temp.append((real, t))
    return temp[-1][0]                      # 가장 뒤에 있는 문자열 출력


N = int(input())
commands = [list(sys.stdin.readline().rstrip().split()) for _ in range(N)]
ans = write(commands)
print(ans)