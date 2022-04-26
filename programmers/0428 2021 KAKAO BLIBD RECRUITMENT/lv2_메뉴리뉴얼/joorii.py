from itertools import combinations


def solution(orders, course):
    dic = {}                                    # key: 주문조합, value: 주문한 사람 인덱스
    for idx, order in list(enumerate(orders)):  # (주문 인덱스, 주문메뉴)
        order = list(order)                     # sort 하기 위해 str -> list
        order.sort()                            # 주문내역 알파벳 오름차순 정렬
        for c in course:
            for comb in list(combinations(order, c)):   # 주문 내열에서 가능한 c개의 모든 조합 구하기
                comb = ''.join(comb)
                if dic.get(comb):               # 이미 존재하는 주문조합이면, 주문한 사람만 더해주기
                    dic[comb].add(idx)
                else:
                    dic.setdefault(comb, {idx}) # 새로운 주문 조합일 때, 주문한 사람의 set으로 setdefault.

    ans = {}
    for c in course:
        ans.setdefault(c, [0])      # key: 메뉴 개수, value: [최다주문조합건수(a.k.a 시킨사람), 주문조합 리스트]

    for key, value in dic.items():
        if len(value) >= 2 and len(value) > ans[len(key)][0]:
            ans[len(key)] = [len(value), key]
        elif len(value) >= 2 and len(value) == ans[len(key)][0]:
            ans[len(key)].append(key)

    answer = []
    for c in course:                # 메뉴의 개수가 적은 순서대로
        answer += ans[c][1:]
    answer.sort()                   # 주문조합의 알파벳순 정렬

    return answer


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
# orders = ["XYZ", "XWY", "WXA"]
# course = [2,3,4]
print(solution(orders, course))
