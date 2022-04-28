# 구글링 하라고 낸 문제 같음;;


def solution(info, query):
    cut = {}
    len_query = len(query)
    answer = [0] * len_query
    for i in range(len_query):
        l, e, j, fs = query[i].split(' and ')
        f, s = fs.split()
        cut[(l, e, j, f)] = (int(s), i)

    for application in info:
        language, end, js, food, score = application.split()
        if cut.get((language, end, js, food)):
            if int(score) >= cut[(language, end, js, food)][0]:
                answer[cut[(language, end, js, food)][1]] += 1
        if cut.get(('-', end, js, food)):
            if int(score) >= cut[('-', end, js, food)][0]:
                answer[cut[('-', end, js, food)][1]] += 1
        if cut.get((language, '-', js, food)):
            if int(score) >= cut[(language, '-', js, food)][0]:
                answer[cut[(language, '-', js, food)][1]] += 1
        if cut.get((language, end, '-', food)):
            if int(score) >= cut[(language, end, '-', food)][0]:
                answer[cut[(language, end, '-', food)][1]] += 1
        if cut.get((language, end, js, '-')):
            if int(score) >= cut[(language, end, js, '-')][0]:
                answer[cut[(language, end, js, '-')][1]] += 1
        if cut.get(('-', '-', js, food)):
            if int(score) >= cut[('-', '-', js, food)][0]:
                answer[cut[('-', '-', js, food)][1]] += 1
        if cut.get(('-', end, '-', food)):
            if int(score) >= cut[('-', end, '-', food)][0]:
                answer[cut[('-', end, '-', food)][1]] += 1
        if cut.get(('-', end, js, '-')):
            if int(score) >= cut[('-', end, js, '-')][0]:
                answer[cut[('-', end, js, '-')][1]] += 1
        if cut.get((language, '-', '-', food)):
            if int(score) >= cut[(language, '-', '-', food)][0]:
                answer[cut[(language, '-', '-', food)][1]] += 1
        if cut.get((language, '-', js, '-')):
            if int(score) >= cut[(language, '-', js, '-')][0]:
                answer[cut[(language, end, '-', '-')][1]] += 1
        if cut.get((language, end, '-', '-')):
            if int(score) >= cut[(language, end, '-', '-')][0]:
                answer[cut[(language, end, '-', '-')][1]] += 1
        if cut.get(('-', '-', '-', food)):
            if int(score) >= cut[('-', '-', '-', food)][0]:
                answer[cut[('-', '-', '-', food)][1]] += 1
        if cut.get(('-', '-', js, '-')):
            if int(score) >= cut[('-', '-', js, '-')][0]:
                answer[cut[('-', '-', js, '-')][1]] += 1
        if cut.get(('-', end, '-', '-')):
            if int(score) >= cut[('-', end, '-', '-')][0]:
                answer[cut[('-', end, '-', '-')][1]] += 1
        if cut.get((language, '-', '-', '-')):
            if int(score) >= cut[(language, '-', '-', '-')][0]:
                answer[cut[(language, '-', '-', '-')][1]] += 1
        if cut.get(('-', '-', '-', '-')):
            if int(score) >= cut[('-', '-', '-', '-')][0]:
                answer[cut[('-', '-', '-', '-')][1]] += 1

    print(answer)



'''
def solution(info, query):
    len_query = len(query)
    answer = [0] * len_query
    for i in range(len_query):
        l, e, j, fs = query[i].split(' and ')
        f, s = fs.split()
        for application in info:
            language, end, js, food, score = application.split()
            if language == l or l == '-':
                if end == e or e == '-':
                    if js == j or j == '-':
                        if food == f or f == '-':
                            if int(score) >= int(s):
                                answer[i] += 1

    print(answer)
    return answer
'''

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
         ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])
