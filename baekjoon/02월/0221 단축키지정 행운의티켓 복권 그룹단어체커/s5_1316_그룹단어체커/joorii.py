import sys
sys.stdin = open('M.txt')

T = int(input())

for tc in range(T):
    # 단어의 개수
    N = int(input())
    words = [list(map(str, input())) for _ in range(N)]

    cnt = 0

    for word in words:
        # 그룹 단어
        check_group = []
        # 그룹이 아닌 단어
        check_not_group = []

        for idx in range(len(word)):
            # 그룹 단어와 그룹이 아닌 단어에 모두 속해있지 않을 때, 즉 처음 나온 알파벳일 때
            if word[idx] not in check_group and word[idx] not in check_not_group:
                check_group.append(word[idx])
            # 그룹 단어 리스트에 속해있을 때
            elif word[idx] in check_group:
                # 이전과 연속된 알파벳이라면
                if word[idx - 1] == word[idx]:
                    continue
                # 이전과 다른 알파벳이라면
                else:
                    break
        else:
            cnt += 1

    print(cnt)
