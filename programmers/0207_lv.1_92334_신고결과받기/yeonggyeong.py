#신고결과받기 

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report_dic = {id:[] for id in id_list}
    for rep in set(report):
        rep_p = rep.split(' ')
        report_dic[rep_p[1]].append(rep_p[0])
        
    for key, value in report_dic.items():
        if len(value) >= k :
            for v in value:
                answer[id_list.index(v)] += 1
                
    return answer