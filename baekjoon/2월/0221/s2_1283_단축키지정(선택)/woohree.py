import sys
sys.stdin = open('L.txt')

# 60분


def get_keyword(word):
    global keywords
    new = []
    
    # 수정이 가능하도록 리스트에 문자 하나씩 저장
    for idx in range(len(word)):
        new.append(word[idx])

    # 첫 글자 혹은 공백 이후의 문자가 이미 지정한 단축키가 아니라면, 단축키로 지정하고 탈출!
    for idx in range(len(new)):
        if idx == 0 or new[idx-1] == ' ':
            # 대소문자 구분을 안하기 때문에 .lower() 메소드를 사용해서 소문자로 비교
            if new[idx] != ' ' and new[idx].lower() not in keywords:
                keywords.append(new[idx].lower())
                new[idx] = f'[{word[idx]}]'
                break
                
    # 아직 단축키가 지정안된 경우, 문자를 순서대로 보면서 이미 지정한 단축키가 아니라면, 단축키로 지정하고 탈출!
    if ''.join(new) == word:
        for idx in range(len(new)):
            if new[idx] != ' ' and new[idx].lower() not in keywords:
                keywords.append(new[idx].lower())
                new[idx] = f'[{word[idx]}]'
                break

    return ''.join(new)


T = int(input())
keywords = []
for tc in range(T):
    word = input()
    ans = get_keyword(word)
    print(ans)
# print(keywords)