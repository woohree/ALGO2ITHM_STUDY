import math

def solution(fees, records):

    def calculate_minute(in_time, out_time):
        in_hour, in_minute = map(int, in_time.split(':'))
        out_hour, out_minute = map(int, out_time.split(':'))
        # 입/출차 시간이 같을때
        if in_hour == out_hour:
            minute, hour = out_minute - in_minute, 0
        else:
            hour = out_hour - in_hour
            # 36 분 입차 / 24분 출차와 같은 케이스 처리
            if out_minute < in_minute:
                hour -= 1
                minute = 60 - in_minute + out_minute
            else:
                minute = out_minute - in_minute
        return minute + hour * 60

    def calculate_cost(minutes):
        # 기본 요금 이하일때
        if minutes <= int(fees[0]):
            cost = int(fees[1])
        else:
            minutes -= int(fees[0])
            cost = math.ceil(minutes / int(fees[2])) * int(fees[3]) + int(fees[1])

        return cost

    cars, costs = {}, {}
    for record in records:
        time, number, in_out = record.split()
        # 출차일때
        if in_out == 'OUT':
            costs[number] += calculate_minute(cars[number], time)
            cars.pop(number)
        # 입차일때
        else:
            cars[number] = time
            # 비용 정보 초기화
            if not costs.get(number):
                costs[number] = 0
    # 마지막까지 출차 하지 않은 차 계산
    for k, v in cars.items():
        costs[k] += calculate_minute(v, '23:59')
    # 프린트 편하게 하려고 미리 정렬
    costs = sorted(costs.items())
    answer = []
    for c in costs:
        answer.append(calculate_cost(c[1]))

    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))
