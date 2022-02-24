import sys
sys.stdin = open('G.txt')

def solution(words):
    stack = []
    for word in words:
        # 여는 괄호이면 stack에 추가
        if word == '(' or word == '[':
            stack.append(word)
        # 닫는 괄호
        elif word == ')' or word == ']':
            # 처음부터 닫는 괄호가 나오면 더 돌지 않고 바로 0 반환
            if not(len(stack)):
                return 'no'
            
            # 가장 마지막 여는 괄호 반환
            # 가장 마지막 여는 괄호와 현재 닫는 괄호가 짝을 이루지 않는다면 0 반환
            top = stack.pop()
            if word == ')' and top != '(':
                return 'no'
            elif word == ']' and top != '[':
                return 'no'
    # 닫는 괄호 없는 여는 괄호가 남아있을 경우에도 0 반환
    if len(stack) > 0:
        return 'no' 
    return 'yes'

flag = True
while flag:
    sentence = input()
    if sentence == '.':
        flag = False
        break
    sentences = list(sentence)
    answer = solution(sentences)
    print(answer)