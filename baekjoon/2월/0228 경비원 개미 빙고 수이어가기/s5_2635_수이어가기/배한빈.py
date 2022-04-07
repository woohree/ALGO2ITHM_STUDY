# 40분

# 1. 첫 번째 수로 양의 정수
# 2. 두 번째 수는 양의 정수 중에서 하나를 선택
# 3. i 번째(i>=3)부터 이후에 나오는 모든 수는 i-2 수에서 i-1 수를 빼서 만든다.
# 4. 음의 정수가 만들어지면, 이 음의 정수를 버리고 더 이상 수를 만들지 않는다.

import sys
sys.stdin = open('B.txt')

# 첫번째 인풋값
fst_num = int(input())

# numbers의 길이가 최대인 max_len_numbers를 1로 설정. 첫번째 인풋값은 들어가므로 1보다 항상 크기에
# 자연수를 계산하는거라서 시작점 start는 1로 설정.
max_len_numbers = start = 1

# 시작점이 처번째 인풋값을 넘으면 탈출
while start <= fst_num:
    numbers = [fst_num]

    # i는 start부터 시작점의 +2한 값으로 범위 설정
    for i in range(start, fst_num + 2):
        # for문 초기에 strat를 리스트에 추가
        if i == start:
            numbers.append(start)
        # numbers list의 길이가 2 이상은 되야 계산 가능하므로,
        if len(numbers) >= 2:
            # 이전의 이전 값과 이전 값의 차가 0보다 작으면 for문 탈출
            if numbers[i - start] - numbers[i - start + 1] < 0:
                break
            # 음수가 아니면 리스트에 추가
            else:
                numbers.append(numbers[i - start] - numbers[i - start + 1])
    # 최대값 구하고, 그 때 numbers 리스트를 answer에 저장
    if len(numbers) > max_len_numbers:
        max_len_numbers = len(numbers)
        answer = numbers

    start += 1

print(max_len_numbers)
for i in range(len(answer)-1):
    print(answer[i], end=' ')
print(answer[-1])
