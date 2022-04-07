import sys
sys.stdin = open('G.txt')

# 입력된 리스트의 왼쪽 합과 오른쪽 합 구하기
def make_sum(sub):
    mid = len(sub) // 2
    left_sum = 0
    right_sum = 0
    for k in range(mid):
        left_sum += sub[k]
    for l in range(mid, len(sub)):
        right_sum += sub[l]

    return left_sum, right_sum

def is_lucky_ticket(ticket):
    length = 0
    for i in range(len(ticket)):
        # 행운의 티켓은 2N이기 때문
        for j in range(i+1,len(ticket),2):
            # ticket에서 sub list 생성 -> [7, 4, 2, 3, 3, 2, 8, 5] ==> [7, 4] / [7, 4, 2, 3]
            sub = ticket[i:j+1]
            left_sum, right_sum = make_sum(sub)
            
            if left_sum == right_sum:
                # 최장 길이인지 확인
                if length < len(sub):
                    length = len(sub)
        
    return length

ticket = list(map(int, input()))
answer = is_lucky_ticket(ticket)
print(answer)