import sys
from itertools import permutations
sys.stdin = open('input.txt')

number = [0,1,2,3,4,5,6,7,8,9]

while input != int('0'):
    A = int(input())
    if A == 0:
        break
    # 단어를 리스트로 저장
    words = [list(input()) for _ in range(A)]
    len_word = []
    first_alpha_index = []
    alpha_left_unorderd = []
    alpha_unorderd = []
    first_alpha = []
    for i in range(A-1):
        len_word.append(len(words[i]))
    for i in range(len(len_word)):
        if len_word[i] == 1:
            pass
        elif len_word[0] != 1 and i == 0:
            first_alpha_index.append(0)
        elif len_word[i] != 1:
            first_alpha_index.append(sum(len_word[0:i]))
    for i in range(A-1):
        for j in words[i]:
            alpha_left_unorderd.append(j)
            alpha_unorderd.append(j)
    for i in words[A-1]:
        alpha_unorderd.append(i)
    for i in first_alpha_index:
        first_alpha.append(alpha_left_unorderd[i])
    first_alpha.append(words[A-1][0])
    words_non_repeat = list(set(alpha_unorderd))

    # count

    same = 0

    # 퍼뮤테이션
    for perm in permutations(number, len(set(alpha_unorderd))):
        alpha_dicts = {}
        zero = 0
        for i in range(len(words_non_repeat)):
            if first_alpha.find(words_non_repeat[i]) and perm[i] == 0:
                zero = 1
                continue
            else:
                alpha_dicts[words_non_repeat[i]] = perm[i]
        if zero != 0:
            continue
        left = 0
        right = 0
        for i in range(A-1):
            for j in range(len(words[i])):
                left += alpha_dicts.get(words[i][j])*(10**(len(words[i])-j-1))
        for i in range(len(words[A-1])):
            right += alpha_dicts.get(words[A-1][i])*(10**(len(words[A-1])-i-1))
        if left==right:
            same += 1
    print(same)