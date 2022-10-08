import sys
sys.stdin = open('G.txt')

def make_list(first, second):
    # 첫번째, 두번째 숫자 설정
    numbers = [first, second]
    # 세번째 숫자부터 만들기 위해 설정
    idx = 2
    # 마지막으로 추가된 숫자가 음수일때까지 원소 추가
    while numbers[-1] >= 0:
        numbers.append(numbers[idx-2] - numbers[idx - 1])
        idx += 1
    
    # 마지막 수 제거
    numbers.pop()
    return numbers


n = int(input())

answers = []
length = 0
# n이 1이라면 second_number는 무조건 1이어야 최장 길이 리스트 생성 가능
if n == 1:
    second_number = 1
    numbers = make_list(n, second_number)
    if length <= len(numbers):
        length = len(numbers)
        answers = numbers
else:
    # 1이 아니라면, 첫 숫자에 절반 이상이어야 최대 리스트 생성 가능 ( 절반 이하이면, 4번째 부터 음수 발생 ) 
    for i in range(int(n/2), n):
        second_number = i
        numbers = make_list(n, second_number)
        if length <= len(numbers):
            length = len(numbers)
            answers = numbers

answers = ' '.join(map(str, answers))
print(length)
print(answers)