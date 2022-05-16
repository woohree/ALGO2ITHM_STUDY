import sys
sys.stdin = open('B.txt')

'''
문제 설명 중에 마지막 문단 너무 어렵게 적혀 있는거 같다...
결국엔 출력 2개 하는건데 모르고 최대 길이인 것들 다 출력해서 계속 출력초과뜸
근데 내 풀이 3등 풀이됨 ㅋ

* 로직
1. 단어들의 인덱스를 기억해야 해서 (index, word) 꼴로 words 만들고 알파벳 순으로 정렬
2. 단어의 접두사를 key값으로 하고 value에는 해당 단어들을 갖는 딕셔너리 result를 만듬
3. 단어의 접두사가 이미 result에 저장되어 있는 경우, value에 일단 넣고 index로 정렬한 다음 맨 뒤에 단어 pop시킴
4. result의 values 를 answer_temp에 extends 시키고 다시 index 기준으로 정렬
5. answer_temp의 첫번째 요소를 answer에 넣고 해당 접두사를 뽑아 그 다음 접두사가 일치하는 단어 찾고 break
'''

N = int(sys.stdin.readline().rstrip())
words = []
# 1.
for i in range(N):
    words.append((i, sys.stdin.readline().rstrip()))
words.sort(key=lambda x: x[1])

# 2.
result = {}
my_max = 0
for i in range(N-1):
    word = words[i]
    next_word = words[i+1]
    count = 0
    prefix = ''  # 접두사
    for j in range(len(word[1])):
        if word[1][j] == next_word[1][j]:
            count += 1
            prefix += word[1][j]
        else:
            break
    if my_max <= count:
        if my_max == count:
            # 3.
            if result.get(prefix):
                result[prefix].append(next_word)
                result[prefix].sort()
                result[prefix].pop()
            else:
                result[prefix] = [word, next_word]
        else:
            result.clear()
            result[prefix] = [word, next_word]
            my_max = count

# 4.
answer_temp = []
for k, v in result.items():
    answer_temp.extend(v)
answer_temp.sort()

# 5.
answer = []
check = ''
for a in answer_temp:
    if answer:
        if a[1][:my_max] == check:
            answer.append(a[1])
            break
    else:
        answer.append(a[1])
        check = a[1][:my_max]
print(*answer)
