# 50분

# 키를 정렬하고 인덱스 추출
def sort_key(key):
    # key 리스트화
    key = [char for char in key]

    # 문자 -> 숫자
    nums_key = []
    for char in key:
        num_key = ord(char)
        nums_key.append(num_key)

    # 버블정렬로 오름차순 정렬
    for time in range(len(nums_key) - 1, 0, -1):
        for idx in range(time):
            if nums_key[idx] > nums_key[idx + 1]:
                nums_key[idx], nums_key[idx + 1] = nums_key[idx + 1], nums_key[idx]

    # 숫자 -> 문자
    result_key = []
    for num in nums_key:
        key1 = chr(num)
        result_key.append(key1)

    # 정렬한 키의 인덱스를 추출
    idxs_result_key = []
    for idx2 in range(len(result_key)):
        for idx in range(len(key)):
            # 같은 문자가 있는 경우, 에러를 방지하기 위해 인덱스를 뽑은 문자는 지움
            if key[idx] == result_key[idx2]:
                idxs_result_key.append(idx)
                key[idx] = ''
                break

    return idxs_result_key

# 암호를 받아 표로 반환
def get_table_password(password):
    idx = 0
    # 입력이 열 기준이므로, 행 기준으로 표에 기입
    for col in range(len(key)):
        for row in range(len(password)//len(key)):
            table_password[row][col] = password[idx]
            if idx == len(password) - 1:
                break
            idx += 1
    return table_password

# 정렬한 키 인덱스와 암호 표를 받아, 암호문 해독
def get_real_sentence(sortkey, table):
    # 해독한 암호문의 길이(가로: 키 길이, 세로: 암호문 길이/키 길이)
    real_sentence = [[0] * len(key) for _ in range(len(password)//len(key))]
    # 정렬한 키 인덱스에 맞추어 암호문 재배열(해독)
    for row in range(len(password)//len(key)):
        col = 0
        for number in sortkey:
            real_sentence[row][number] = table[row][col]
            if col == len(key) - 1:
                break
            col += 1

    return real_sentence

key = input()
password = input()
# 암호문 길이 100자 이하 조건에 맞추어 빈 테이블 생성
table_password = [[0] * 10 for _ in range(10)]

a = sort_key(key)
b = get_table_password(password)

# 출력조건에 맞춤
# 행마다 .join을 사용
ans = get_real_sentence(a, b)
for sentence in ans:
    final_ans = ''.join(sentence)
    print(final_ans, end='')

