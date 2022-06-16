import sys
sys.stdin = open('B.txt')

N = int(sys.stdin.readline().rstrip())
memory = {0: ''}
result = ''
for _ in range(N):
    order, text, sec = sys.stdin.readline().rstrip().split()
    sec = int(sec)
    if order == 'type':
        result += text
    else:
        text = int(text)
        a = memory.keys()
        for key in a:
            if key >= sec - text - 1:
                result = memory[key]
                break
        else:
            result = ''
    memory[sec] = result

print(result)

'''
def undo(sec, text):
    for _ in range(int(text)):
        if result and result[-1][1] + 3 >= sec:
            if result[-1][2] == 'type':
                stack.append(result.pop())
            elif result[-1][2] == 'undo':
                if result[-1][3]:
                    pass
                else:
                    stack.append(result.pop())
                    undo(stack[-1][1], stack[-1][0])


N = int(sys.stdin.readline().rstrip())

result = []
stack = []
check = 0
for _ in range(N):
    result.sort(key=lambda x: x[1])
    order, text, s = sys.stdin.readline().rstrip().split()
    sec = int(s)
    if order == 'type':
        result.append((text, sec, order))
    else:
        check += 1
        undo(sec, text)
        result.append([int(text), sec, order, check%2])
for r in result:
    if r[2] == 'type':
        print(r[0], end='')
'''
