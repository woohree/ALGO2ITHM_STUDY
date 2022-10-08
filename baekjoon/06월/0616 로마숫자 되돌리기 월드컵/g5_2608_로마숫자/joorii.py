import sys
sys.stdin = open('M.txt')

romans = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

decimals = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M',
}


def roman_to_dec(roman_num):
    num_sum = 0
    num_idx = len(roman_num) - 1

    while num_idx >= 0:     # 오른쪽에서부터 시작
        if num_idx > 0 and romans[roman_num[num_idx - 1]] < romans[roman_num[num_idx]]:   # 왼쪽 숫자가 더 작을 때
            num_sum += romans[roman_num[num_idx]] - romans[roman_num[num_idx - 1]]
            num_idx -= 2
        else:
            num_sum += romans[roman_num[num_idx]]
            num_idx -= 1

    return num_sum


def dec_to_roman(dec_num):
    d_list = [1, 5, 10, 50, 100, 500, 1000]
    str_num = str(dec_num)
    rom_num = ''        # 로마 숫자
    num_idx = 0
    num_len = len(str_num) - 1

    while num_idx <= num_len:     # 왼쪽에서부터 시작
        temp_num = int(str_num[num_idx]) * 10 ** (num_len - num_idx)      # num_idx 자리수의 숫자

        if temp_num == 0:       # 0일떄는 continue
            num_idx += 1
            continue

        temp = (num_len - num_idx) * 2
        for idx in range(temp, temp + 3):
            if idx < 7:
                if temp_num // d_list[idx] < 4 and temp_num % d_list[idx] < 4 * 10 ** (num_len - num_idx):
                    plus_char = (temp_num % d_list[idx]) // 10 ** (num_len - num_idx)       # 오른쪽에 더해질 숫자 개수
                    rom_num += decimals[d_list[idx]] * (temp_num // d_list[idx])
                    rom_num += decimals[d_list[temp]] * plus_char
                    break
                elif d_list[idx + 1] % temp_num == 10 ** (num_len - num_idx):       # 4 또는 9일 떄, 즉 왼쪽에 숫자가 더해질 때
                    rom_num += decimals[d_list[temp]] + decimals[d_list[idx + 1]]
                    break

        num_idx += 1

    return rom_num


one = input()
two = input()

dec_num = roman_to_dec(one) + roman_to_dec(two)
print(dec_num)
print(dec_to_roman(dec_num))
