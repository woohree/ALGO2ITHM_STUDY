# 60분 시도 시간초과 실패 ㅜㅜ
import sys
sys.stdin = open('M.txt')


def key_logger():
    stack = []
    idx = -1

    for char in text:
        if char == '<':
            if idx >= 0:
                idx -= 1
        elif char == '>':
            if idx < len(stack) - 1:
                idx += 1
        elif char == '-':
            if idx >= 0:
                stack.pop(idx)
                idx -= 1
        # 방향키 이외의 글자가 들어왔을 때
        else:
            # 가장 마지막에 추가
            if idx + 1 == len(stack):
                stack.append(char)
            # 중간에 추가
            else:
                stack.insert(idx + 1, char)
            idx += 1

    for char in stack:
        print(char, end='')
    print()


T = int(input())

for tc in range(1, T + 1):
    text = list(map(str, input()))

    key_logger()
