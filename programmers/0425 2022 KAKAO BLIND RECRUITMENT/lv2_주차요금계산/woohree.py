import math


# 30분
def solution(fees, records):
    basic_time, basic_fee, unit_time, unit_fee = fees

    cars = {}
    for record in records:
        temp, car, flag = record.split()
        hour, minute = list(map(int, temp.split(':')))
        time = hour*60 + minute                         # 시간 데이터 분 단위로 가공

        if flag == 'IN':                                # 입차라면, 키 = 차 번호, 값 = 빈 리스트 생성
            cars.setdefault(car, []).append(time)       # 이미 입차했던 차라면, 차 번호에 시간 추가!
        else:
            cars[car].append(time)                      # 출차라면, 차 번호 시간 추가!

    answer = []
    for car, times in cars.items():
        if len(times) % 2:                              # 홀수번 들락날락했다면, 마지막 출차 기록(23:59) 추가!
            times.append(1439)

        total_time = 0                                  # 출차 시간 - 입차 시간 = 주차 시간
        for i in range(1, len(times), 2):
            total_time += times[i] - times[i-1]

        fee_time = total_time - basic_time
        if fee_time > 0:                                # 주차 요금 계산
            fee = basic_fee + math.ceil(fee_time/unit_time) * unit_fee
            answer.append([car, fee])
        else:                                           # 기본 요금
            answer.append([car, basic_fee])

    answer.sort()                                       # 차 번호 기준으로 오름차순 정렬
    answer = list(map(lambda x: x[1], answer))          # 차 번호는 빼고, 주차 요금만 출력!
    return answer


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))