import sys
sys.stdin = open('G.txt')

def get_locations(w, h, directions):
    # 1 : 북 2 : 남 3 : 서 4: 동
    # 모서리들을 하나의 리스트로 생각 ( 북 동 남 서 순서 )
    locations = []
    for direction in directions:
        # 북쪽
        if direction[0] == 1:
            locations.append(direction[1])
        # 동쪽
        elif direction[0] == 4:
            locations.append(w + direction[1])
        # 남쪽
        elif direction[0] == 2:
            locations.append(w + h + w - direction[1])
        # 서쪽
        else:
            locations.append(2 * w + h + h - direction[1])

    user = locations.pop()

    return user, locations

def get_distance(w, h, user, locations):
    min_distance = 0
    for location in locations:
        # 시계방향
        clock = abs(user - location)
        # 빈시계방향 -> 전체 길이에서 시계방향의 길이만큼 제외
        re_clock = 2*(w+h) - clock

        if clock < re_clock:
            min_distance += clock
        else:
            min_distance += re_clock
        
    return min_distance
        
w, h = map(int, input().split())
n = int(input())
directions = [list(map(int, input().split())) for _ in range(n+1)]

user, locations = get_locations(w, h, directions)
answer = get_distance(w, h, user, locations)
print(answer)