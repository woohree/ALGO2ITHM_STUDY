import sys
sys.stdin = open('L.txt')

# 30분
# 입력방식때문에 시간 좀 걸림
# 추가로, ([ (([( [ ] ) ( ) (( ))] )) ]). 이 조건이 무슨 뜻인가 no인 줄 알고 하루 종일 고민함

def is_balanced_sentence(sentence):
    # 판별을 도와줄 스택 리스트 생성
    stack = []
    # sentence의 문자 하나하나 검사
    for char in sentence:
        if char == '(':
            stack.append('()')
        elif char == ')':
            # 이전에 괄호가 열리지 않았거나 혹은 []가 닫히지 않은 경우
            if stack == [] or stack[-1] == '[]':
                return 'no'
            stack.pop()

        elif char == '[':
            stack.append('[]')
        elif char == ']':
            # 이전에 괄호가 열리지 않았거나 혹은 ()가 닫히지 않은 경우
            if stack == [] or stack[-1] == '()':
                return 'no'
            stack.pop()


    # 스택이 비어있으면 True!
    if stack == []:
        return 'yes'
    # 스택에 인자가 남아있다면 False!
    else:
        return 'no'

while 1:
    sentence = input()
    if sentence == '.':
        break
    print(is_balanced_sentence(sentence))