
key = input()
coding = input()
# 한 줄에 몇개의 문자가 들어가야할지 구하기 위해 line을 구하기
lines = len(coding) // len(key)

# key 값을 정렬하기 위해 ascii 코드로 변경
def to_ascii(string):
    ord_list = []
    for i in string:
        ord_list.append(ord(i))
    return ord_list

# ascii 값 버블 정렬하기
def bubble_sort(lst):
    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

# ascii 를 다시 string으로 변경
def to_string(ascii):
    chr_list = []
    for j in ord_list:
        chr_list.append(chr(j))
    return chr_list

ord_list = to_ascii(key)
ord_list_sort = bubble_sort(ord_list) 
chr_list = to_string(ord_list_sort)

# column을 기준으로 lines 개수만큼 리스트에 추가
# EIAAHEBXOIFWEHRXONNAALRSUMNREDEXCTLFTVEXPEDARTAXNAARYIEX / line이 4라면 [EIAA], [HEBX] ...~
coding_lst = []
for i in range(0, len(coding), lines):
    coding_lst.append(list(coding[i:i+lines]))

# 정렬한 key 리스트와 key의 한 문자열씩 반복
# 만약, 정렬된 key 리스트의 값과 같다면, 새로 생성한 answers 에 담아주고, 중복되는것을 방지하기 위해 정렬된 key 값을 숫자로 변경 후 다음 key 문자로 넘어가기
answers = []
for k in key:
    for idx, zip_list in enumerate(zip(chr_list,coding_lst)):
        if k == zip_list[0]:
            answers.append(zip_list[1])
            chr_list[idx] = '99'
            break

for i in range(lines):
    for j in answers:
        print(j[i], end='')    
    
