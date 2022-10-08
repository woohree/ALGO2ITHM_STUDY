from itertools import permutations
import sys
sys.stdin = open('M.txt')


def weight_loss():
    perms = list(permutations(range(N), N))
    count = 0

    for perm in perms:
        # 중량의 디폴트값 0
        weight = 0
        for p in perm:
            # 기존 중량 + 중량 증가량 - 매일 감소량
            if weight + weights[p] - K < 0:
                break
            weight = weight + weights[p] - K
        # 모든 운동 키트를 한 번씩 사용한 후, 즉, N일이 지난 후
        else:
            if weight >= 0:
                count += 1

    return count


N, K = map(int, input().split())
weights = list(map(int, input().split()))
print(weight_loss())
