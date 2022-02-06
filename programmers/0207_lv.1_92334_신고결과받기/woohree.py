def solution(id_list, report, k):
    
    answer = [0] * len(id_list)
    set_reports = []
    for re in set(report):
        set_reports.append(re.split())

    id_dict = {x: 0 for x in id_list}
    
    for reports in set_reports:
        id_dict[reports[1]] += 1

    for reports in set_reports:
        if id_dict[reports[1]] >= k:
            answer[id_list.index(reports[0])] += 1

    return answer