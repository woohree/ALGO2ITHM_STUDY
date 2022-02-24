import sys
sys.stdin = open('L.txt')

# 30분

def get_password(keylog, N):
    real_password = []  # 진짜 비밀번호 저장
    temp = []           # 임시 저장소

    for i in range(N):
        # '-' => 백스페이스, 진짜 비밀번호에서 pop!
        if keylog[i] == '-':
            if real_password == []:
                continue
            else:
                real_password.pop()

        # '<', '>' => 방향키,
        # 왼쪽으로 갈 때는 진짜 비밀번호에서 마지막 거 지우고 임시 저장소에 추가
        # 오른쪽으로 갈 때는 임시 저장소에서 마지막 거 지우고 진짜 비밀번호에 추가
        elif keylog[i] == '<':
            if real_password == []:
                continue
            else:
                temp.append(real_password.pop())
        elif keylog[i] == '>':
            if temp == []:
                continue
            else:
                real_password.append(temp.pop())

        # 그 외, 그냥 추가
        else:
            real_password.append(keylog[i])

    # 마지막에 임시 저장소에 뭔가 남아 있다면, 마지막 거 부터 진짜 비밀번호에 순서대로 추가
    if temp != []:
        for _ in range(len(temp)):
            real_password.append(temp.pop())

    return ''.join(real_password)


T = int(input())

for tc in range(T):
    keylog = input()
    N = len(keylog)
    ans = get_password(keylog, N)
    print(ans)
