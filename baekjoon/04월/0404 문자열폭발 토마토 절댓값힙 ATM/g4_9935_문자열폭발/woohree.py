import sys
sys.stdin = open('L.txt')


def mine_bomb():
    result = []
    l = len(mine)

    for i in range(len(chars)):
        result.append(chars[i])                             # result에 문자 추가
        if chars[i] == mine[-1] and result[-l:] == mine:    # 추가한 문자와 폭발 문자열의 마지막 문자가 같고,
            for _ in range(l):                              # result의 마지막 문자열이 폭발 문자열과 같다면,
                result.pop()                                # pop!

    if result:
        return ''.join(result)
    return 'FRULA'


chars = input()
mine = list(input())
ans = mine_bomb()
print(ans)