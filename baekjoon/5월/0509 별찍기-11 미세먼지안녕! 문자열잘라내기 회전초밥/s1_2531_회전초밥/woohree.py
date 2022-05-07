import sys
sys.stdin = open('L.txt')


N, d, k, c = map(int, input().split())
sushi = {}
plates = []

for _ in range(N):
    temp = int(sys.stdin.readline().rstrip())
    plates.append(temp)                 # 초밥 접시 리스트
    sushi.setdefault(temp, 0)           # 초밥 종류 딕셔너리
sushi.setdefault(c, 0)                  # 주방장이 쿠폰 초밥 안내놨을 경우가 있음

for i in range(k-1):                    # 회전해야 하니까, 초밥 접시 리스트 뒤에 k-1개 순서대로 더 붙여줌
    plates.append(plates[i])

l = r = 0                               # 좌, 우 포인터
ans = plate_cnt = sushi_cnt = 0         # 출력값, 먹은 접시 카운트, 초밥 종류 카운트
while l < N:
    if plate_cnt == k:                  # k번 연속으로 먹은 경우,
        sushi[plates[l]] -= 1           # 딕셔너리에서, 먹은 접시 중 제일 왼쪽에 있는거 안먹었다고 바꾸기
        if not sushi[plates[l]]:        # 스시 값이 0이면 안먹은 거,
            sushi_cnt -= 1              # 초밥 종류 -1
        l += 1                          # 좌측 포인터 +1
        plate_cnt -= 1                  # 먹은 접시 -1

    else:                               # 아직 k번 못 채운 경우,
        if not sushi[plates[r]]:        # 안먹은 거면,
            sushi_cnt += 1              # 초밥 종류 +1
        sushi[plates[r]] += 1           # 딕셔너리에서, 먹은 접시 중 제일 오른쪽에 있는거 먹었다고 체크
        r += 1                          # 우측 포인터 +1
        plate_cnt += 1                  # 먹은 접시 +1

    if sushi_cnt >= ans:                # 같은거 포함안하면, 밑에 쿠폰 초밥 체크를 못함
        ans = sushi_cnt
        if not sushi[c]:
            ans += 1

print(ans)