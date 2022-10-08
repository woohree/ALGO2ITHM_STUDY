import sys
from itertools import combinations
sys.stdin = open('B.txt')

L, C = map(int, sys.stdin.readline().rstrip().split())
alphabets = sys.stdin.readline().rstrip().split()
alphabets.sort()
comb = list(combinations(alphabets, L))
vowels = ['a', 'e', 'i', 'o', 'u']
for c in comb:
    count_vowel, count_consonant = 0, 0
    for alphabet in c:
        if alphabet in vowels:
            count_vowel += 1
        else:
            count_consonant += 1
        if count_vowel >= 1 and count_consonant >= 2:
            print(''.join(c))
            break
