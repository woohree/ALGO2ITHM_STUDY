# 2:45 시작 3:30 완성 => 45분 소요
# 1부터 N까지의 수 중에 서로 다른 M개의 수
# K개의 수가 같으면 당첨
# 2 ≤ N ≤ 8
# 1 ≤ M ≤ N-1
# 1 ≤ K ≤ M

# N개 중 M개 뽑아서 K개가 같으면 당첨...
# '3 2 1'에서 1~3 중 2개 뽑아서(1 3, 2 3, 1 2) 1개라도 같으면 당첨 => 100%
# 내가 뽑은 경우랑 리조트에서 뽑은 거랑 비교

# 조합 모듈
from itertools import combinations

import sys
sys.stdin = open('B.txt')

N, M, K = map(int, input().split())
numbers = [i for i in range(1, N + 1)]

# my_numbers와 your_numbers 리스트에 combinations 써가지고 나올 수 있는 경우 저장
# list이므로 같이 선언하고 my_numbers에만 append 써도 같이 기록됨
my_numbers = your_numbers = []
for i in list(combinations(numbers, M)):
    my_numbers.append(i)

# 당첨된 경우들 카운팅
win = 0
for my_number in my_numbers:
    for your_number in your_numbers:
        # 문자 하나씩 비교
        count = 0
        for i in my_number:
            for j in your_number:
                # 문자가 같은 때마다 count로 기록
                # 같은 숫자 찾으면 다시 같은 숫자가 나올 일이 없으므로 break로 빠져나옴
                if i == j:
                    count += 1
                    break
        # count가 K보다 크거나 같으면 당첨
        if count >= K:
            win += 1

# my_numbers와 your_numbers의 길이가 같으므로 그냥 my_numbers 제곱해서 win을 나누면 확률 나옴
print(win / len(my_numbers) ** 2)
