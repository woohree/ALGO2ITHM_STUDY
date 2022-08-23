import sys
sys.stdin = open('input.txt')

from collections import deque
def solution(cacheSize, cities):
    # cacheSize가 없으면 계속 cacheMiss가 나므로 그냥 5를 곱한 값을 반환
    if cacheSize == 0:
        return (5*len(cities))
    # 총 걸리는 시간
    answer = 0

    for i in range(len(cities)):
        cities[i] = cities[i].lower()
    cache = deque()
    for i in range(len(cities)):
        if cities[i] in cache:
            cache.remove(cities[i])
            cache.append(cities[i])
            answer += 1
        else:
            if len(cache) == cacheSize:
                cache.popleft()
                cache.append(cities[i])
            elif len(cache) < cacheSize:
                cache.append(cities[i])
            answer += 5
    return answer