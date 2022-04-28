from itertools import combinations


def solution(orders, course):
    # 정답의 배열을 담을 리스트
    answer = []

    for c in course:
        dic = dict()
        # 모든 주문에서 c개의 조합을 찾기
        for order in orders:
            if len(order) >= c:
                for comb in combinations(list(order), c):
                    # 알파벳 정렬후 dic에 추가
                    comb = ''.join(sorted(comb))
                    if not dic.get(comb):
                        dic[comb] = 1
                    else:
                        dic[comb] += 1
        # 최대 주문된 메뉴 조합찾기
        if dic:
            max_count = max(dic.values())
            if max_count >= 2:
                for k, v in dic.items():
                    if v == max_count:
                        answer.append(k)
    answer.sort()
    return answer


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
print(solution(orders, course))
