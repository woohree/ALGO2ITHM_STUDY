from collections import Counter

# 실패!실패~~!!
def solution(info, query):
    answer = []
    dict = {}
    for i in range(len(info)):
        temp = info[i].split(' ')
        score = int(temp[-1])
        for data in temp:
            if not data.isdecimal():
                dict.setdefault(data, []).append((score, i))
    for key, values in dict.items():
        dict[key] = sorted(values, reverse=True)
    # print(dict)
    for q in query:
        q = q.replace('and', '')
        q = q.split()
        _cnt = 0
        q_list = []
        q_score = int(q[-1])
        for i in range(4):
            if q[i] == '-':
                _cnt += 1
            else:
                tt = set()
                for j in range(len(dict[q[i]])):
                    # print(dict[q[i]][j][1])
                    if dict[q[i]][j][0] < q_score:
                        break
                    tt.add(dict[q[i]][j])
                q_list.append(tt)

        # print(q_list)
        if q_list:
            a = q_list[0]
            for i in range(len(q_list)):
                a &= q_list[i]
            answer.append(len(a))
        else:
            cnt = 0
            for qqq in query:
                qqq = qqq.split()
                qqq_score = int(qqq[-1])
                if qqq_score >= q_score:
                    cnt += 1
            answer.append(cnt)
    return answer


info=["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query=["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))