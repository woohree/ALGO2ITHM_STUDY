import sys
sys.stdin = open('L.txt')


def who_is_conqueror(armies):
    army_dict = {}                              # 군대명: 병사 수
    conqueror = max_army = 0                    # 정복한 군대명, 가장 많은 병사 수

    for army in armies:                         # 병사들 돌면서,
        army_dict.setdefault(army, 0)           # 군대명 키가 없다면, 군대명: 0 으로 생성
        army_dict[army] += 1                    # 있으면, 병사 수 +1

    for army in army_dict:                      # army_dict 돌면서,
        k = army_dict[army]
        if k > n//2 and k > max_army:           # 전체 수의 절반보다 크고, 병사 수가 가장 많다면,
            max_army = k                        # 가장 많은 병사 수 갱신
            conqueror = army                    # 새로운 정복자 탄생
        elif k == max_army:                     # 가장 많은 병사 수가 동일하다면,
            return 'SYJKGW'                     # 'SYJKGW'

    if not conqueror:                           # 정복자가 없다면,
        return 'SYJKGW'                         # 'SYJKGW'

    return conqueror


N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    n, *armies = map(int, sys.stdin.readline().rstrip().split())
    ans = who_is_conqueror(armies)
    print(ans)
