from collections import Counter
import itertools
#
def solution(orders, course):
    answer = []

    for n in course:
        temp = []
        for order in orders:
            order = sorted(list(order))
            temp.extend(list(itertools.combinations(order, n)))

        # flags1 = Counter(temp)
        flags = {}                              # 리스트에서 같은 값을 키로, 중복 횟수를 값으로 만든 딕셔너리
        for t in temp:
            flags.setdefault(t, 0)
            flags[t] += 1
        # print(flags1)
        # print(flags)
        ans = 2
        ans_lst = []
        for key, values in flags.items():
            if values >= ans:                   # 최댓값보다 크거나 같다면,
                if values > ans:                # 더 큰 경우,
                    ans = values                # 값 갱신,
                    ans_lst = []                # 리스트 초기화
                ans_lst.append(''.join(key))    # 어펜드
        answer.extend(ans_lst)

    answer.sort()
    return answer


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
print(solution(orders, course))

# def solution(orders, course):
#     answer = []
#     menus = {}
#     temp = set()
#     for i in range(len(orders)):
#         for menu in orders[i]:
#             temp.add(menu)
#             menus.setdefault(menu, set()).add(i+1)
#     # print(menus)
#     t = list(temp)
#     real = []
#     for i in t:
#         if len(menus[i]) > 1:
#             real.append(i)
#
#     for n in course:
#         max_len = 2
#         max_lst = []
#
#         combs = list(itertools.combinations(real, n))
#         print(combs)
#         for comb in combs:
#             temp_set = set(menus[comb[0]])
#             for i in range(1, n):
#                 temp_set &= menus[comb[i]]
#             l = len(temp_set)
#             if l >= max_len:
#                 if l > max_len:
#                     max_len = l
#                     max_lst = []
#                 ans = ''.join(sorted(list(comb)))
#                 max_lst.append(ans)
#
#         answer.extend(max_lst)
#     answer.sort()
#
#     return answer