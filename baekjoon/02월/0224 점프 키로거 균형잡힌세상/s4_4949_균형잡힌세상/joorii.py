# 20분
import sys
sys.stdin = open('M.txt')


def check_pair(word):
    open_bracket = []

    for char in word:
        # 왼쪽 괄호가 들어왔을 때 추가하기
        if char == '(' or char == '[':
            open_bracket.append(char)
        elif char == ')':
            if len(open_bracket) != 0 and open_bracket[-1] == '(':
                open_bracket.pop()
            else:
                return 'no'
        elif char == ']':
            if len(open_bracket) != 0 and open_bracket[-1] == '[':
                open_bracket.pop()
            else:
                return 'no'

    if len(open_bracket) == 0:
        return 'yes'
    else:
        return 'no'


while 1:
    text = list(map(str, input()))

    if text == ['.']:
        break

    print(check_pair(text))
