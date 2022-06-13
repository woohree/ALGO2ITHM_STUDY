from itertools import combinations
import sys
sys.stdin = open('M.txt')


def make_code():
    result = set()
    vowels = {'a', 'e', 'i', 'o', 'u'}
    v = chars.intersection(vowels)      # 모음 set
    c = chars.difference(vowels)        # 자음 set

    selected_vs = list(combinations(v, 1))      # 모음 1개 조합
    selected_cs = list(combinations(c, 2))      # 자음 2개 조합

    for selected_v in selected_vs:
        for selected_c in selected_cs:
            remains = v.difference(selected_v).union(c.difference(selected_c))      # 선택된 조합 이외 나머지
            selected_rs = list(combinations(remains, L - 3))        # 나머지 L - 3개 조합
            for selected_r in selected_rs:
                temp = ''.join(sorted(selected_v + selected_c + selected_r))
                result.add(temp)

    for code in sorted(list(result)):
        print(code)


# 서로 다른 L개의 알파벳 소문자, 문자의 종류 C가지
L, C = map(int, sys.stdin.readline().split())
chars = set(map(str, sys.stdin.readline().split()))
make_code()
