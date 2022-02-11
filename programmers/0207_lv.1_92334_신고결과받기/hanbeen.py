def solution(id_list, report, k):
    report = set(report)  # 중복값 지우기
    report = list(report)
    
    new_list = []
    for i in report:
        new_list.append(i.split(' ')) 
    
    id_dic = {}
    for i in range(len(id_list)):
        id_dic[id_list[i]] = 0
    
    for key, value in id_dic.items():
        for i in range(len(report)):
            if key == new_list[i][1]:
                id_dic[key] += 1
    
    bad_users = []
    for key, value in id_dic.items():
        if value >= k:
            bad_users.append(key)
    
    singoja = []
    for i in new_list:
        if i[1] in bad_users:
            singoja.append(i[0])
    
    result = {}
    for i in range(len(id_list)):
        result[id_list[i]] = 0
    
    for key, value in result.items():
        for i in range(len(singoja)):
            if key == singoja[i]:
                result[key] += 1
    
    return list(result.values())
        
solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)