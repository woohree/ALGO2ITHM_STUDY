'''
코드가 너무 길어... 그래서 속도가 너무 느려..
1. 코스에 나와있는 요리 개수를 이용하여 order 에서 요리 개수 만큼의 조합을 만듬
2.  다름 사람과겹치게 되는 조합이라면 result 딕셔너리에 저장
3. 코스에 명시된 요리 개수 당 가지는 조합들 중 가장 자주 나온 조합들 구함

그래도 예제 다 푸니 한번에 통과
'''


from itertools import combinations


def solution(orders, course):
    orders2 = []
    result = {}
    # 1, 2번 내용
    while orders:
        current = orders.pop()
        for num in course:
            comb = list(combinations(current, num))
            for c in comb:
                c = sorted(c)
                current_len = len(c)
                check = 0
                for order in orders:
                    order_len = len(order)
                    if order_len >= current_len:
                        temp = 0
                        for i in range(order_len):
                            for j in range(current_len):
                                if order[i] == c[j]:
                                    temp += 1
                                    break
                            if temp == current_len:
                                check += 1
                                break
                for order in orders2:
                    order_len = len(order)
                    if order_len >= current_len:
                        temp = 0
                        for i in range(order_len):
                            for j in range(current_len):
                                if order[i] == c[j]:
                                    temp += 1
                                    break
                            if temp == current_len:
                                check += 1
                                break
                c = ''.join(c)
                if check >= 1:
                    if result.get(c):
                        if result[c] < check:
                            result[c] = check
                    else:
                        result[c] = check
        orders2.append(current)

    # 3번
    temp_max_courses = {}
    answer = []
    for number in course:
        for k, v in result.items():
            len_b = len(k)
            if len_b == number:
                if temp_max_courses.get(v):
                    temp_max_courses[v].append(k)
                else:
                    temp_max_courses[v] = [k]
        keys = temp_max_courses.keys()
        if keys:
            # 질문 : 이 부분 줄일 수 있나
            # for i in temp_max_courses[max(keys)]:
            #     answer.append(i)

            answer.extend(temp_max_courses[max(keys)])

        temp_max_courses = {}
    print(sorted(answer))
    return sorted(answer)


solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5])
