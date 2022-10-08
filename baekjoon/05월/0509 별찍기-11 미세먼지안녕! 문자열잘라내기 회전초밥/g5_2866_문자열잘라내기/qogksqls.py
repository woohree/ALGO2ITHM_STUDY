# 50분
import sys
sys.stdin = open('B.txt')


'''
시간초과 미치것네;;

좀 억울하다.. python3로 돌리다가 시간초과 계속 나서 pypy로 돌리면 통과할 떄가 있고
pypy로 돌리다가 python3로 돌리면 통과할 때가 있다..

1. 일단 세로 문자열을 쫙 만들었다. 근데 pop을 쓰고 싶어서 순서는 뒤바꿔서 만들었다.
2. 그 다음 check라는 set 만들어서 세로 문자열에서 pop 해준걸 넣었다. 그럼 중복값이 있다면 사라질 것이다.
3. C와 check의 길이를 비교해서 같으면 +1하고 다르면 break했다. 
'''

R, C = map(int, sys.stdin.readline().rstrip().split())
strings = [sys.stdin.readline().rstrip() for _ in range(R)]
'''
# 1번
sero_strings = []
for c in range(C):
    s = []
    for r in range(R-1, -1, -1):
        s.append(strings[r][c])
    sero_strings.append(s)

count = 0
while 1:
    # 2번
    check = set()
    for i in range(C):
        sero_strings[i].pop()
        temp = ''.join(sero_strings[i])
        check.add(temp)

    # 3번
    if C == len(check):
        count += 1
    else:
        break

print(count)
'''
'''
# 1등 코드... 이분법 쓴거같은데 뭔소린지;;디버깅이나 보여드림
strings = list(zip(*strings))
top, bottom = 0, C - 1
ans = 0
while top <= bottom:
    mid = (top + bottom) // 2
    words = set()
    for j in range(C):
        word = ''.join(strings[j][mid:])
        if word in words:
            break
        words.add(word)
    else:
        ans = mid
        top = mid + 1
        continue
    bottom = mid - 1
print(ans)
'''