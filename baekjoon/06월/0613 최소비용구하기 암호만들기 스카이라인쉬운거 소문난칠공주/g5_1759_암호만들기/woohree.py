import sys, itertools
sys.stdin = open('L.txt')


def make_passwords(alps):
    for temp_password in list(itertools.combinations(alps, L)):     # 경우의 수 그냥 다 파악!
        cnt_vowel = cnt_consonant = 0                               # 모음, 자음 수 파악
        for char in temp_password:
            if char in ['a', 'e', 'i', 'o', 'u']:
                cnt_vowel += 1
            else:
                cnt_consonant += 1

        if cnt_vowel > 0 and cnt_consonant > 1:
            real_password = ''.join(temp_password)
            print(real_password)                                    # 조건에 맞으면 출력


L, C = map(int, input().split())
alps = input().split()
alps.sort()                                                         # 먼저 정렬!
make_passwords(alps)