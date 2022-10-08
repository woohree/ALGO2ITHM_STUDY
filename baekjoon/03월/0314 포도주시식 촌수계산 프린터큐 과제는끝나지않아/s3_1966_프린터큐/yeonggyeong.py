import sys
sys.stdin = open('G.txt')


def get_order(importances):
    # target인지 확인하기 위한 list 생성
    idx = list(range(n))
    # 몇 번째로 인쇄되는지 count
    cnt = 0

    while True:
        # 중요도들 사이의 최댓값 찾기
        max_importance = 0
        for importance in importances:
            if importance > max_importance:
                max_importance = importance

        # 최댓값이 첫번째 값과 같다면 count +=1
        if importances[0] == max_importance:
            cnt += 1
            # 그 값이 타겟값과 같다면 count 반환
            if idx[0] == m:
                return cnt
            else:
                # 아니라면 출력 완료
                importances.pop(0)
                idx.pop(0)
        else:
            # 최댓값이 아니라면 리스트 뒤에 새로 추가
            importances.append(importances.pop(0))
            idx.append(idx.pop(0))


T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    importances = list(map(int, input().split()))
    answer = get_order(importances)
    print(answer)