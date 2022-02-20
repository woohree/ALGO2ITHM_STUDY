# 3:45 시작 => 4:50 완성... 65분 소요
# 행운의 티켓은 N자리
# 왼쪽 N자리의 합과 오른쪽 N자리의 합이 일치
# 문자열의 연속된 부분 문자열 중 행운의 티켓 규칙을 만족하는 최대 부분 문자열의 길이를 출력
# 문자열 S는 1보다 크거나 같고, 9보다 작거나 같은 수로 이루어짐
# len(S) <= 50
# 행운의 티켓 규칙을 만족하는 부분 문자열의 최대 길이를 출력
# 찾을 수 없다면 0을 출력

# '74233285' => 7423 3285 => 16 18
# => 2332 => 4
# 짝수길이, 8 찾고 6찾고 4 찾고 2 찾고

import sys
sys.stdin = open('B.txt')

S = list(map(int, input()))
length = len(S)

while length >= 1:
    # S의 길이가 홀수일 때 1을 빼줘서 짝수 길이로 만든다.
    if length % 2:
        length -= 1

    # 범위의 시작점 0으로 설정
    # while문을 돌수록 시작점이 변동된다.
    start = 0
    while length + start <= len(S):
        lucky_ticket = []
        left_sum = right_sum = 0

        # 주어진 범위에서 S의 요소들을 lucky_ticket 리스트에 저장
        for i in range(start, length + start):
            lucky_ticket.append(S[i])

        # 반으로 쪼개서 왼쪽 오른쪽 따로 더함
        for i in range(length // 2):
            left_sum += lucky_ticket[i]
            right_sum += lucky_ticket[i + (length // 2)]

        # 왼쪽과 오른쪽의 합이 같으면 while문을 탈출하고 아니면 시작점에 1 더함
        if left_sum == right_sum:
            break
        start += 1

    # 왼쪽과 오른쪽의 합이 같으면 안쪽 while문을 탈출했을거고 한번 더 while문을 탈출하기 위해 선언
    # 안 같으면 전체 길이 length를 2씩 줄여줌
    if left_sum == right_sum:
        break
    length -= 2

# 왼쪽과 오른쪽이 합이 결국 같지 않았거나 S의 길이가 1일 때는
# lucky_ticket을 빈 스트링으로 선언함으로써 값이 0이 나오도록 설정
if left_sum != right_sum or len(S) == 1:
    lucky_ticket = ''

print(len(lucky_ticket))
