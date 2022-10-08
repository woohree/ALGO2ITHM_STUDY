import sys
sys.stdin = open('M.txt')


def check_first_char(option):
    idx = 0
    for word in option:
        if word[0].lower() not in short_keys:
            short_keys.append(word[0].lower())
            short_keys_idx.append(idx)
            return 1
        idx += len(word) + 1

    return 0


def check_short_key(option):
    idx = 0

    for word in option:
        for i in range(1, len(word)):
            idx += 1
            if word[i].lower() not in short_keys:
                short_keys.append(word[i].lower())
                short_keys_idx.append(idx)
                return 1
        idx += 2

    return 0


T = int(input())

for tc in range(T):
    N = int(input())
    options = [list(map(str, input().split())) for _ in range(N)]

    short_keys = []
    short_keys_idx = []

    for option in options:
        # 모든 단어의 첫 글자에서 단축키를 찾았을 때
        if check_first_char(option) == 1:
            continue
        # 왼쪽부터 차례대로 단축키 지정
        elif check_short_key(option) == 1:
            continue
        # 단축키를 지정할 수 없을 때
        else:
            short_keys.append(None)
            short_keys_idx.append(-1)

    # 출력 조건에 맞게 프린트 :: short_key_idx에 해당하는 수 앞 뒤로 대괄호 출력
    for i in range(len(options)):
        result = ' '.join(options[i])
        for j in range(len(result)):
            if j == short_keys_idx[i]:
                print(f'[{result[j]}]', end='')
            else:
                print(result[j], end='')
        print()
