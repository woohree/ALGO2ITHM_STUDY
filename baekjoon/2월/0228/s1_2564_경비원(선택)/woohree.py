import sys
sys.stdin = open('input.txt')


# 아 심신미약온다 어지럽다 어지러워
# 동근이 위치 기준으로 돌면서 거리구함
# 헷갈리다 헷갈리고 헷갈려서 시간이 너무 오래 걸림
def get_distance(market, security):
    if security[0] == 1:  # 북동근
        location_now = h + (w-security[1])
        if market[0] == 2:  # 반대편
            distance1 = abs(location_now - (market[1] + 2*h + w))
            distance2 = abs(location_now + (w-market[1]))
            if distance1 <= distance2:
                return distance1
            return distance2
        elif market[0] == security[0]:  # 같은편
            return abs(location_now - ((w-market[1]) + h))
        elif market[0] == 4:  # 동
            return abs(location_now - (h-market[1]))
        else:  # 서
            return abs(location_now - (market[1] + h + w))

    if security[0] == 2:  # 남동근
        location_now = h + security[1]
        if market[0] == 1:  # 반대편
            distance1 = abs(location_now - ((w-market[1]) + 2*h + w))
            distance2 = abs(location_now + market[1])
            if distance1 <= distance2:
                return distance1
            return distance2
        elif market[0] == security[0]:  # 같은편
            return abs(location_now - (market[1] + h))
        elif market[0] == 3:  # 서
            return abs(location_now - market[1])
        else:  # 동
            return abs(location_now - ((h-market[1]) + h + w))

    if security[0] == 3:  # 서동근
        location_now = w + (h-security[1])
        if market[0] == 4:  # 반대편
            distance1 = abs(location_now - ((h-market[1]) + h + 2*w))
            distance2 = abs(location_now + (h-market[1]))
            if distance1 <= distance2:
                return distance1
            return distance2
        elif market[0] == security[0]:  # 같은편 
            return abs(location_now - ((h-market[1]) + w))
        elif market[0] == 2:  # 남
            return abs(location_now - (w-market[1]))
        else:  # 북
            return abs(location_now - (market[1] + h + w))

    if security[0] == 4:  # 동동근
        location_now = w + security[1]
        if market[0] == 3:  # 반대편
            distance1 = abs(location_now - ((w-market[1]) + h + 2*w))
            distance2 = abs(location_now + market[1])
            if distance1 <= distance2:
                return distance1
            return distance2
        elif market[0] == security[0]:  # 같은편 
            return abs(location_now - (market[1] + w))
        elif market[0] == 1:  # 북
            return abs(location_now - market[1])
        else:  # 남
            return abs(location_now - ((w-market[1]) + h + w))


w, h = list(map(int, input().split()))
N = int(input())
markets = [list(map(int, input().split())) for _ in range(N)]
security = list(map(int, input().split()))
distance = 0
for market in markets:
    distance += get_distance(market, security)
print(distance)