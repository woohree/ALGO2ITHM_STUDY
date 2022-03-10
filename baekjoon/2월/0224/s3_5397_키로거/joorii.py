# 60분 시도 시간 초과 실패 ㅜㅜ
import sys
sys.stdin = open('M.txt')


def key_logger():
    left = []
    right = []

    for char in text:
        if char == '<' and left:
            right.append(left.pop())
        elif char == '>' and right:
            left.append(right.pop())
        elif char == '-' and left:
            left.pop()
        # 알파벳 혹은 숫자가 들어 왔을 때
        elif char.isalpha() or char.isdigit():
            left.append(char)

    return ''.join(left + right[::-1])


T = int(input())

for tc in range(T):
    text = input()

    print(key_logger())
