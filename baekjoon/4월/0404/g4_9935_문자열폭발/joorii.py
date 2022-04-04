import sys
sys.stdin = open('M.txt')


def explode():
    stack = []
    i = 0
    while i < len(inputs):
        stack.append(inputs[i])
        if inputs[i] == bomb[-1] and ''.join(stack[-len(bomb):]) == bomb:   # 폭발 문자열의 마지막 단어가 들어왔을 때, 스택에 쌓인 뒷 부분을 확인
            for _ in range(len(bomb)):
                stack.pop()
        i += 1
    if not stack:
        return 'FRULA'
    return ''.join(stack)


inputs = input()
bomb = input()
print(explode())
