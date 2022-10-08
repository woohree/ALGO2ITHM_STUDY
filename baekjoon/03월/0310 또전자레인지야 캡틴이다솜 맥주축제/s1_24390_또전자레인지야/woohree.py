import sys
sys.stdin = open('L.txt')


def again(time):
    result = time[0]%10 + time[0]//10       # 10분 버튼 + 나머지 1분 버튼
    if time[1] >= 30:                       # 30초 이상인 경우, 조리 시작부터 누르고 본다.
        result += 1 + (time[1]-30)//10      # 조리시작(30초) + 10초 버튼
        return result
    else:
        result += time[1]//10               # 30초 미만인 경우, 다 누르고 시작 버튼을 눌러야 한다.
        return result+1                     # 그래서 +1


time = list(map(int, sys.stdin.readline().rstrip().split(':')))
ans = again(time)
print(ans)