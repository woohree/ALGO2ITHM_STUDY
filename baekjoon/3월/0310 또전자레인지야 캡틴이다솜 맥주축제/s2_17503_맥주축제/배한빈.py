# 하루에 맥주 1병
# 도수 높으면 맥주 마시다 기절ㅋㅋㅋㅋ
# 선호도, 도수 레벨, 간 레벨
# 맥주 N개의 선호도 합이 M 이상
# 조건을 만족하는 간 레벨의 최솟값을 출력하는 프로그램

# K개 중 N개 마셔야 함, M도 채워야 함
# 정렬하고 선호도가 낮은 맥주부터 N개씩 채우는데 M을 넘을 때 조사.

# 40
# 시간초과 나서 sort() 쓴걸 바꿔야겠다싶었음

# 정렬을 굳이 안쓰고 해보기
#


import sys
sys.stdin = open('B.txt')

# 일단 시간이 급해서 인터넷에서 퀵솔트 복붙해서 돌려봤는데 정렬이 잘됨
# 그래서 백준에서 돌려보니 이것도 시간초과가 나옴.
def quick_sort(array, start, end):
    # 원소가 1개인 경우 종료
    if start >= end:
        return

    pivot = start  # pivot은 첫 번째 원소
    left = start + 1
    right = end

    # 엇갈리기 전까지 반복
    while left <= right:
        # pivot보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1

        # pivot보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1

        # 엇갈렸다면 작은 데이터와 pivot을 스와핑
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 다시 퀵 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


N, M, K = map(int, input().split())

beers = [list(map(int, input().split())) for _ in range(K)]
# beers.sort()
quick_sort(beers, 0, len(beers)-1)
# [[1, 4], [2, 5], [3, 3], [4, 3], [4, 6]]

dosu = []
# N = 3, K = 5 이므로 i는 2,3,4
for i in range(N-1, K):
    preference = 0
    for j in range(N):
        preference += beers[i-j][0]

    if M <= preference:
        dosu.append(beers[i-2][1])
        dosu.append(beers[i-1][1])
        dosu.append(beers[i][1])
        break

# 코드 자체는 정답이 아닐거 같은데 일단 시간초과가 뜨니까 검사도 못하고 넘김..

if dosu:
    print(max(dosu))
else:
    print(-1)
