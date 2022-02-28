import sys
sys.stdin = open('G.txt')


def get_password(input_key):
    left_s = []
    right_s = []

    for key in input_key:
        # 입력 문자일때 
        if key not in ['<', '>', '-']:
            left_s.append(key)
        
        # < 이고, left_s가 비어있지 않을때
        # left_s의 최신값을 right_s에 추가 ( 왼쪽으로 커서 이동 )
        elif key == '<':
            if left_s:
                right_s.append(left_s.pop())

        # > 이고, right_s가 비어있지 않을때
        # right_s 최신값을 left_s 추가 ( 오른쪽으로 커서 이동 )
        elif key == '>':
            if right_s:
                left_s.append(right_s.pop()) 

        # -이고, left_s가 비어있지 않을때
        # left_s의 최신값을 삭제 (왼쪽값을 삭제하기 때문에 left_s에서 삭제)
        elif key == '-':
            if left_s:
                left_s.pop()

    # right는 가장 최신의 값부터 출력해야하기 때문에 역방향으로 더하기
    password = left_s + right_s[::-1]
    password = ''.join(password)

    return password


T = int(input())

for tc in range(T):
    input_key = input()
    answer = get_password(input_key)
    print(answer)