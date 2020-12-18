# This will open a text file, split it into a list of each line
file = open('advent-day-18.txt',newline='')
inputdata = file.read().splitlines()
sample = ['1 + 2 * 3 + 4 * 5 + 6','5 + (8 * 3 + 9 + 3 * 4 * 3)','5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))']


# This funtion cleans the strings in the input data, removing whitespace,
# adding * for multiplication, and wrapping each statement in a set of parens
def prep_strings(inputdata):
    outputdata = []
    for line in inputdata:
        temp = line.replace('  ','*').replace(' ','')
        outputdata.append('(' + temp + ')')
    return outputdata


# This function evaluates an innermost string of operations (ie no parens) with no operator precedence.
# It evaluates the string of operations left to right, regardless of + or *
# There is an extra step in this, because it's reading numbers as strings, it must first
# identify the end of a multi-digit number before performing the operation.
def no_prec_eval(string):
    result = '0'
    operator = '+'
    chars = ''
    for idx, char in enumerate(string):
        if char in ['+','*']:
            operator = char
        else:
            chars = chars + char
            if idx < len(string)-1 and string[idx+1] not in ['+','*']:
                pass
            else:
                result = str(eval(result + operator + chars))
                chars = ''
    return result


# This function evaluates an innermost string of operations (ie no parens) with addition precedence.
# By replacing '*' with ')*(', all additions will be evaluated first,
# but it first needs an extra set of outer parens to prevent open brackets
def add_prec_eval(string):
    string = '(' + string + ')'
    string = string.replace('*',')*(')
    result = str(eval(string))
    return result


# This function evaluates an innermost string of operations (ie no parens) with multiplication precedence.
# This is how math normally works.
def multiply_prec_eval(string):
    result = str(eval(string))
    return result


# This function reduces a string by a single innermost set of parens.
# It finds the first ')' and then identifies the string preceding it.
# It then applies the appropriate evaluation function to that string,
# and replaces the original string with the result.
# Calling this function many times will eventually reduce a string to a single value.
def eval_parens(string, precedence):
    for idx, char in enumerate(string):
        if char == '(':
            left = idx + 1
        elif char == ')':
            right = idx
            if precedence == '+':
                result = add_prec_eval(string[left:right])
            elif precedence == '*':    
                result = multiply_prec_eval(string[left:right])
            else:
                result = no_prec_eval(string[left:right])
            return string.replace('('+string[left:right]+')',result)


# This function evaluates a string by calling eval_parens until it has reduced the string completely
def string_evaluator(string, precedence):
    while '(' in string:
        string = eval_parens(string, precedence)
    return string


# This function evalutes a list of math strings, then returns the sum of their results
def maths_sum(stringlist, precedence = None):
    total = 0
    for string in stringlist:
        total += int(string_evaluator(string, precedence))
    return total


# Solutions
mathlist = prep_strings(inputdata)
print('Solution to Part 1:\n',maths_sum(mathlist, None))
print('\nSolution to Part 2:\n',maths_sum(mathlist, '+'))
