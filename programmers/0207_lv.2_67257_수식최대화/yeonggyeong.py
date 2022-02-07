import re
def solution(expression):
    answer = 0
    combinations = [['+','-','*'],['+','*','-'],['-','+','*'],['-','*','+'],['*','-','+'],['*','+','-']]
    # for combination in combinations:
    operand = re.split('[*+-]',expression)
    operator = re.split('[0-9]+',expression)
        
        
    
    return operator, operand

print(solution('500*200-144'))