import sys
sys.stdin = open('G.txt')

def get_beer(beers):
    global n, m, k

    preferences = []
    min_prefer = 999
    min_index = 0
    for index, beer in enumerate(beers):
        preferences.append(beer)
        if beer[0] < min_prefer:
            min_prefer = beer[0]
            min_index = index
        # 마신 맥주의 개수가 n 과 같다면
        if len(preferences) == n:
            # 선호도 계산
            sum = 0
            for preference in preferences:
                sum += preference[0]
            # 선호도가 최소 선호도보다 높다면 도수 출력
            if sum >= m:
                return preferences
            elif sum < m and index != len(beers)-1:
                preferences.pop(min_index)
            else:
                return -1

n, m, k = map(int, sys.stdin.readline().rstrip().split())

# 선호도 도수 [선호도,도수]
beers = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(k)]
# 도수를 기준으로 정렬
# beers.sort(key = lambda x:(x[1], x[0]))

answers = get_beer(beers)
if answers == -1:
    print(answers)
else:
    alcohol = 999
    for answer in answers:
        if answer[1] > alcohol:
            alcohol = answer[1]

    print(answer)