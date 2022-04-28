# 효율성 테스트 시간초과
def solution(info, query):
    qualified = {}          # key: 인덱스, value: [개발언어, 직군, 경력, 소울푸드, 자격요건]
    for q in list(enumerate(query)):
        idx, lst = q[0], q[1].split(' ')
        qualified[idx] = []
        for l in lst:
            if l != 'and':
                qualified[idx].append(l)

    answer = [0 for _ in range(len(query))]

    for key, values in qualified.items():
        for data in info:
            d = data.split(' ')
            for i in range(5):
                if i == 4 and int(d[i]) >= int(values[i]):  # 코딩테스트 기준 점수 이상일 때
                    answer[key] += 1
                if values[i] != '-' and values[i] != d[i]:
                    break

    return answer


info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]
print(solution(info, query))
