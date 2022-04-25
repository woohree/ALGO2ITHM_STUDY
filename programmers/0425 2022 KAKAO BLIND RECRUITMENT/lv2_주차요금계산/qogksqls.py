# fees = [1, 461, 1, 10]
# records = ["00:00 1234 IN"]

fees = [120, 0, 60, 591]
records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]

import math

# 차 번호를 key, 출입 정보와 시간을 value 값으로 갖는 cars 딕셔너리 생성
cars = {}
for record in records:
    # input 가공
    t, numbers, in_out = record.split()
    h, m = map(int, t.split(':'))
    time = h * 60 + m

    if cars.get(numbers):
        if cars[numbers][0] == 1:
            if len(cars[numbers]) == 2:
                cars[numbers] = [0, time - cars[numbers][1]]
            else:
                cars[numbers] = [0, cars[numbers][1] + (time - cars[numbers][2])]
        # 하루에 2번씩 왔다 갔다 하는 녀석들
        # value의 list 마지막에 n번 입장 했을 때의 시간을 저장
        else:
            cars[numbers] = [1, cars[numbers][1], time]
    else:
        cars[numbers] = [1, time]  # value값의 첫번째 값이 1이면 IN, 0이면 OUT을 나타낸다.

# 최종적으로 cars 는 차 번호를 key 값으로 갖고
# value 의 list 는 [출입 정도(0 or 1), 주차 이용 시간 or 처음 입장한 시간, 마지막으로 입장한 시간]

# 차 번호를 기준으로 오름차순 정렬
car_numbers = list(cars.items())
car_numbers.sort(key=lambda x: x[0])  # [('0202', [0, 120]), ('3961', [1, 120, 1438])]

end = 23 * 60 + 59  # 23:59을 분으로 바꾼 값
# 차 번호가 작은 순서대로
for car_number in car_numbers:
    # 마지막이 IN 이었던 차
    if car_number[1][0] == 1:
        if len(car_number[1]) == 2:
            car_number[1].append(end - car_number[1][1])
        else:
            car_number[1].append(car_number[1][1] + end - car_number[1][2])  # ('3961', [1, 120, 1438, 121])
    
    # 최종 주차 요금 정산
    if car_number[1][-1] > fees[0]:
        car_number[1].append(fees[1] + math.ceil((car_number[1][-1] - fees[0]) / fees[2]) * fees[3])
    else:
        car_number[1].append(fees[1])

# 출력
result = []
for car_number in car_numbers:
    result.append(car_number[1][-1])

print(result)
