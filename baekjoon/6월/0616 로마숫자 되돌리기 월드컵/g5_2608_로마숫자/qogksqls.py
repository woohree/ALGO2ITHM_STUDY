import sys
sys.stdin = open('B.txt')

Roma_numbers = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
# 아라비안 숫자로
input_numbers = []
for _ in range(2):
    r = input()
    input_number = []
    for n in r:
        input_number.append(Roma_numbers[n])
    for i in range(len(input_number)-1):
        if input_number[i] != 0 and input_number[i] < input_number[i+1]:
            input_number[i] = input_number[i+1] - input_number[i]
            input_number[i+1] = 0
    input_numbers.append(sum(input_number))
result = str(sum(input_numbers))
print(result)

# 로마 숫자로
Roma_number = []
len_result = len(result)
for j in range(len_result):
    if result[j] == '4':
        if len_result - j - 1 == 0:
            Roma_number.append('IV')
        elif len_result - j - 1 == 1:
            Roma_number.append('XL')
        elif len_result - j - 1 == 2:
            Roma_number.append('CD')
    elif result[j] == '9':
        if len_result - j - 1 == 0:
            Roma_number.append('IX')
        elif len_result - j - 1 == 1:
            Roma_number.append('XC')
        elif len_result - j - 1 == 2:
            Roma_number.append('CM')
    elif result[j] == '1':
        if len_result - j - 1 == 0:
            Roma_number.append('I')
        elif len_result - j - 1 == 1:
            Roma_number.append('X')
        elif len_result - j - 1 == 2:
            Roma_number.append('C')
        elif len_result - j - 1 == 3:
            Roma_number.append('M')
    elif result[j] == '2':
        if len_result - j - 1 == 0:
            Roma_number.append('II')
        elif len_result - j - 1 == 1:
            Roma_number.append('XX')
        elif len_result - j - 1 == 2:
            Roma_number.append('CC')
        elif len_result - j - 1 == 3:
            Roma_number.append('MM')
    elif result[j] == '3':
        if len_result - j - 1 == 0:
            Roma_number.append('III')
        elif len_result - j - 1 == 1:
            Roma_number.append('XXX')
        elif len_result - j - 1 == 2:
            Roma_number.append('CCC')
        elif len_result - j - 1 == 3:
            Roma_number.append('MMM')
    elif result[j] == '5':
        if len_result - j - 1 == 0:
            Roma_number.append('V')
        elif len_result - j - 1 == 1:
            Roma_number.append('L')
        elif len_result - j - 1 == 2:
            Roma_number.append('D')
    elif result[j] == '6':
        if len_result - j - 1 == 0:
            Roma_number.append('VI')
        elif len_result - j - 1 == 1:
            Roma_number.append('LX')
        elif len_result - j - 1 == 2:
            Roma_number.append('DC')
    elif result[j] == '7':
        if len_result - j - 1 == 0:
            Roma_number.append('VII')
        elif len_result - j - 1 == 1:
            Roma_number.append('LXX')
        elif len_result - j - 1 == 2:
            Roma_number.append('DCC')
    elif result[j] == '8':
        if len_result - j - 1 == 0:
            Roma_number.append('VIII')
        elif len_result - j - 1 == 1:
            Roma_number.append('LXXX')
        elif len_result - j - 1 == 2:
            Roma_number.append('DCCC')
print(''.join(Roma_number))
