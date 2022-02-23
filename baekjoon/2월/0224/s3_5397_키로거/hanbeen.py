# 1.35 + 10:25
# 키보드로 입력한 키는 알파벳 대문자, 소문자, 숫자, 백스페이스, 화살표
# 만약 커서의 위치가 줄의 마지막이 아니라면,
# 커서 및 커서 오른쪽에 있는 모든 문자는 오른쪽으로 한 칸 이동한다.

# 계속해서 시간초과(50%)때문에 패스가 안됩니다.
# 처음에 del 써서 그런거 같아 pop()으로 다 수정했는데도 그대로입니다.
# append와 pop은 O(1)이라 작은 시간 복잡도를 갖고 있고, 어디서 문제인지...
# input()을 sys.stdin.readline()으로 바꿔서 제출해봤는데 그대로
# deque도 빠르다그랬는데 안됨.. 연결리스트 써야할거같은데 너무 귀찮다.

import sys
sys.stdin = open('B.txt')

from collections import deque

T = int(sys.stdin.readline())
for tc in range(1, T+1):
    sentence = deque(list(sys.stdin.readline()))
    L = len(sentence)

    password = deque([])
    count = 0
    for word in sentence:
        if word == '<':
            # password가 True일 경우, len(password) - count이 0보다는 커야하는 조건 하에 카운트 한다.
            if password:
                if len(password) - count > 0:
                    count += 1

        elif word == '>':
            # password가 True일 경우, count - 1이 0보다는 크거나 같아야 하는 조건 하에 빼준다.
            if password:
                if count - 1 >= 0:
                    count -= 1

        elif word == '-':
            # pop()으로 마지막 값 뺀다.
            if password:
                password.pop()

        else:
            if count == 0:
                # sys.stdin.readline()을 쓰면 마지막에 '\n'이 같이 출력돼서 안 나오게끔 조건 설정
                if word != '\n':
                    password.append(word)
                else:
                    break
            # count가 0이 아니면 위치를 바꿔줘야 한다는 뜻
            else:
                password.append(word)
                for c in range(1, count + 1):
                    password[len(password) - c], password[len(password) - c - 1] = password[len(password) - c - 1], password[len(password) - c]

    password = ''.join(password)
    print(password)
