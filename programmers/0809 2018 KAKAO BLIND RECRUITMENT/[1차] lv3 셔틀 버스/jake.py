# 최대 길이 2000이면 우선 정렬 가능
def solution(n, t, m, timetable):
    # 분단위로 변환해줌(제일 늦은 시간 구해야 해서)
    for idx, time in enumerate(timetable):
        minute, second = time.split(':')
        timetable[idx] = int(minute) * 60 + int(second)
    # 무작위로 시간이 있으니 순서대로 시간을 바꿔줌
    timetable = sorted(timetable)
    # (시간, 탑승자, 마지막 탑승시간)
    mydict = [[540 + i * t, int(m), 0] for i in range(n)]
    # 시간 인덱스, 탑승 인덱스
    time_idx, mydict_idx = 0, 0
    while True:
        # 마지막
        if time_idx == len(timetable) or mydict_idx == n:
            break
        # 탑승자리가 있고 시간이 맞을때
        if mydict[mydict_idx][1] > 0 and timetable[time_idx] <= mydict[mydict_idx][0]:
            mydict[mydict_idx][2] = timetable[time_idx]
            mydict[mydict_idx][1] -= 1
            time_idx += 1
        else:
            mydict_idx += 1
    # 마지막 탑승시간
    if mydict[-1][1] == 0:
        answer = mydict[-1][2] - 1
    else:
        answer = mydict[-1][0]
    # 시간 형태로 다시 변경해서 리턴
    return "%02d:%02d"%(answer//60, answer%60)