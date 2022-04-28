from bisect import bisect_left

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

def solution(info, query):

    queries = [['cpp', 'java', 'python', '-'], ['backend', 'frontend', '-'], ['junior', 'senior', '-'], ['chicken', 'pizza', '-']]

    # 모든 조합 저장하기
    dic = {}
    for language in queries[0]:
        for job in queries[1]:
            for career in queries[2]:
                for food in queries[3]:
                    dic[language+job+career+food] = []

    # 정보에 해당하는 조합에 점수 더해주기
    for i in info:
        language, job, career, food, score = i.split()
        for l in [language, '-']:
            for j in [job, '-']:
                for c in [career, '-']:
                    for f in [food, '-']:
                        information = l + j + c + f
                        dic[information].append(int(score))

    # 정렬 이진탐색을 위해
    for key in dic.keys():
        if dic[key] != []:
            dic[key].sort()

    answer = []
    cnt = 0
    for q in query:
        q = q.split(" ")
        q_info, q_score = q[:-1], int(q[-1])
        q_info = ''.join(q_info).replace("and", "").replace(" ","")
        # score가 들어갈 수 있는 가장 왼쪽 자리
        location = bisect_left(dic[q_info], q_score)
        # cnt += len(dic[q_info][location:])
        cnt += len(dic[q_info]) - location
        # for s in dic[q_info]:
        #     if s >= q_score:
        #         cnt += 1
        answer.append(cnt)
        cnt = 0

    return answer


print(solution(info, query))