from itertools import combinations
import sys
sys.stdin = open('G.txt')

L, C = map(int, sys.stdin.readline().split())
strings = list(sys.stdin.readline().rstrip().split())
strings.sort()

vowels = ['a', 'e', 'o', 'u', 'i']

for comb in list(combinations(strings, L)):
    vowel_cnt = len(set(comb) & set(vowels))      # 모음 개수 세기

    if vowel_cnt >= 1 and (L-vowel_cnt) >= 2:     # 모음 1개 이상 자음 2개 이상일때,
        print(''.join(comb))