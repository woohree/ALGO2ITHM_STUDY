import math


def solution(fees, records):
    car = {}            # 차량 번호 key, IN & OUT 시간 values
    total_time = {}     # 차량 번호 key, 누적 주차 시간 values
    for record in records:              # 차량 번호별 주차 출입 시간 딕셔너리 초기화
        time, num, context = map(str, record.split())
        if num not in car:
            car.setdefault(num, [time])
            total_time.setdefault(num, 0)   # 차량 번호별 key만 미리 생성
        else:
            car[num].append(time)

    for key, values in car.items():         # 누적 주차 시간 구하기
        if len(values) % 2:                 # 출입 시간이 모두 적혀있지 않을 때
            values.append("23:59")
        for i in range(len(values) // 2):
            hour_1, min_1 = map(int, values[i * 2].split(':'))
            hour_2, min_2 = map(int, values[i * 2 + 1].split(':'))

            hour = hour_2 - hour_1
            minute = min_2 - min_1
            if minute < 0:
                minute = 60 + minute
                hour -= 1

            total_time[key] += (60 * hour + minute)

    price = []              # 차량 번호 순 정렬을 위한 리스트화 및 주차 요금 계산    [차량 번호, 일 주차 요금]
    for key, value in total_time.items():
        if value <= fees[0]:            # 기본 시간 이하일 때
            price.append([key, fees[1]])
        else:                           # 기본 시간 초과일 때
            value -= fees[0]
            unit = math.ceil(value / fees[2])
            price.append([key, fees[1] + unit * fees[3]])

    price.sort(key=lambda x: int(x[0]))     # 차량 번호 순 정렬

    answer = []
    for each in price:
        answer.append(each[1])

    return answer