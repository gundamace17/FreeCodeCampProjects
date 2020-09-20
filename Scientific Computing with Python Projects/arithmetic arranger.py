# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 19:14:00 2020

@author: gunda
"""
def arithmetic_arranger(problems, bol = False):
    if len(problems) > 5:
        return "Error: Too many problems."
    upper = []
    bott = []
    total = []
    seperator = []
    
    for i in range(len(problems)):
        cal = problems[i].split()
    
        if len(cal[0]) > 4 or len(cal[-1]) > 4:
            return "Error: Numbers cannot be more than four digits."
          
        if not cal[0].isnumeric() or not cal[-1].isnumeric():
            return 'Error: Numbers must only contain digits.'
        
        if cal[1] == '*' or cal[1] == '/':
            return "Error: Operator must be '+' or '-'."
        
        elif cal[1] == '+':
            leng = max(len(cal[0]), len(cal[2])) + 2
            top = str(cal[0]).rjust(leng)
            bottom = cal[1] + str(cal[2]).rjust(leng - 1)
            total.append(str(int(cal[0]) + int(cal[-1])).rjust(leng))
            upper.append(top)
            bott.append(bottom)
            seperator.append('-' * leng)
        elif cal[1] == '-':
            leng = max(len(cal[0]), len(cal[2])) + 2
            top = str(cal[0]).rjust(leng)
            bottom = cal[1] + str(cal[2]).rjust(leng - 1)
            total.append(str(int(cal[0]) - int(cal[-1])).rjust(leng))
            upper.append(top)
            bott.append(bottom)
            seperator.append('-' * leng)
        
    print('    '.join(upper))
    print('    '.join(bott))
    print('    '.join(seperator))
    
    if bol == True:
        print('    '.join(total))
    
    arranged_problems = '    '.join(upper) + '\n' + '    '.join(bott) + '\n' + '    '.join(seperator)

    if bol == True:
        arranged_problems += '\n'
        arranged_problems += '    '.join(total)
        
    print(arranged_problems)
    return arranged_problems
    

    
arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True)