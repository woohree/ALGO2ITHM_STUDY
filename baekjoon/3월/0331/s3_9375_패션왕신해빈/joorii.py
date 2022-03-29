from itertools import combinations
import sys
sys.stdin = open('M.txt')

T = int(input())

for tc in range(T):
    # 해빈이가 가진 의상의 수 N
    N = int(input())
    clothes_dict = {}
    for _ in range(N):      # 의상의 종류별로 이름을 담은 dict 초기화
        name, type = map(str, input().split())
        clothes_dict.setdefault(type, {None})   # 공집합인 경우도 포함해야하기 때문에 None을 default 값으로 설정
        clothes_dict[type].add(name)

    result = 1
    for key in clothes_dict.keys():     # 의상 종류별로 1개씩 고르는 경우의 수를 구함
        result *= len(list(combinations(clothes_dict[key], 1)))

    print(result - 1)       # 공집합들의 조합 제외
