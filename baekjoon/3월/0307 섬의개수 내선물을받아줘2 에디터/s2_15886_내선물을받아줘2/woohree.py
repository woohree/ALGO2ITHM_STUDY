import sys
sys.stdin = open('L.txt')


# 문제를 좀 헷갈리게 써놨네...
# 길 잃은 접근 => 구사과씨가 두번째줄 명령대로 움직이는 줄 앎
# 옳은 접근 => 명령이 아니라 발판이므로, 구사과씨 시작 지점만 랜덤지정
# 길 잃은 시간 45분 + 푼 시간 5분 ㅡㅡ
# 그냥 EW연속으로 나오면 구사과씨가 멈춤 => EW 갯수만 세면 됨
def count_visited(directions):
    cnt = 0
    for idx in range(N-1):
        if directions[idx] == 'E' and directions[idx+1] == 'W':
            cnt += 1
    return cnt


N = int(input())
directions = [char for char in input()]
ans = count_visited(directions)
print(ans)