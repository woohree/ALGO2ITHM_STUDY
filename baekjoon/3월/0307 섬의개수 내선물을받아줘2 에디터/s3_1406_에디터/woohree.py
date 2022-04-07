import sys
sys.stdin = open('L.txt')

# 어이없네 진짜
# 풀이는 이전 키로거와 거의 동일
# input() 과 sys.stdin.readline() 의 차이는 모르겠지만 후자를 택하니 통과...


def text_editor(text, edit):
    temp = []

    for char in edit:
        if char == 'L':  # 커서 왼쪽으로 이동 => text에서 하나 pop하고 temp에 하나 push
            if text:
                temp.append(text.pop())
        elif char == 'B':  # 지우기 => text에서 하나 pop
            if text:
                text.pop()
        elif char == 'D':  # 커서 오른쪽으로 이동 => temp에서 하나 pop하고 text에 하나 push
            if temp:
                text.append(temp.pop())
        else:  # 그 외, 문자 text에 push
            text.append(char)

    return ''.join(text+temp[::-1])  # temp에 뭐가 남았다면 커서가 문자열 끝이 아님 => text에 temp 역순으로 push


text = [char for char in sys.stdin.readline().rstrip()]
M = int(sys.stdin.readline().rstrip())
edit = []
for _ in range(M):
    a = sys.stdin.readline().rstrip().split()
    if a[0] == 'P':
        edit.append(a[1])
    else:
        edit.append(a[0])
ans = text_editor(text, edit)
print(ans)
