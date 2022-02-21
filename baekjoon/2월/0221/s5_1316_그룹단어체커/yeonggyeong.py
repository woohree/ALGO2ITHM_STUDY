import sys
sys.stdin = open('G.txt')

# string에서 전 알파벳과 다르다면, results 리스트에 추가
# results 예시 'abbccddda' -> [a, b, c, d, a] / 'abccdd' -> [a, b, c, d]
# 만약 results와 set(string)의 길이가 같다면 그룹단어 count +1
def find_group_word(string, group_word):
    results = [string[0]]
    for st in string[1:]:
        if st != results[-1]:
            results.append(st)

    if len(results) == len(set(string)):
        group_word += 1

    return group_word

n = int(input())
group_word = 0

for _ in range(n):
    word = input()
    group_word = find_group_word(word, group_word)

print(group_word)