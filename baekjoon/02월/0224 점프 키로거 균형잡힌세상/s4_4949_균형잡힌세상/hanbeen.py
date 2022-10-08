# 3:50 시작 4:35
# 소괄호, 대괄호
# 입력의 종료조건으로 맨 마지막에 점 하나(".")가 들어온다.

import sys
sys.stdin = open('B.txt')

while 1:
    sentence = input()
    # whlie문을 돌리며 input이 '.'만 있으면 while문 종료
    if sentence == '.':
        break

    # 괄호를 넣어둘 list
    parentheses = []
    for word in sentence:
        # word가 마침표가 나오면 for문 종료
        if word == '.':
            break

        # 여는 괄호 나오면 parentheses에 저장
        elif word == '(':
            parentheses.append(word)
        elif word == '[':
            parentheses.append(word)

        # 닫는 괄호 나오면
        elif word == ')':
            # parentheses가 True이거나 마지막 값이 '('일 때 parentheses의 마지막 값 삭제
            if parentheses and parentheses[-1] == '(':
                del parentheses[-1]
            # 위 조건에 맞지 않으면 list에 word 추가하고 break
            else:
                parentheses.append(word)
                break
        elif word == ']':
            if parentheses and parentheses[-1] == '[':
                del parentheses[-1]
            else:
                parentheses.append(word)
                break

    # parentheses가 True라면 'no', False라면 'yes'
    if parentheses:
        print('no')
    else:
        print('yes')
