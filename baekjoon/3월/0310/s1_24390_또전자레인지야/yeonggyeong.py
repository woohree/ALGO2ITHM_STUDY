import sys
sys.stdin = open('G.txt')

string = list(map(int, input().split(':')))

cnt = 0
# 10분 단위로 나누어진다면
while string[0] // 10:
    cnt += 1
    string[0] -= 10

if string == [0, 0] and cnt != 0:
    cnt += 1
    print(cnt)

# 1분 단위로 나누어진다면
while string[0] // 1:
    cnt += 1
    string[0] -= 1

if string == [0, 0] and cnt != 0:
    cnt += 1
    print(cnt)

if string[0] == 0 and string[1] == 30:
    print(1)

while string[0] == 0 and string[1] // 10:
    cnt += 1
    string[1] -= 10

if string == [0, 0] and cnt != 0:
    cnt += 1
    print(cnt)