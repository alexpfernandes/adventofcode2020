# This will open a text file, split it into a list of each line
file = open('advent-day-19.txt',newline='')
inputdata = file.read().splitlines()
sample = ['0: 4 1 5','1: 2 3 | 3 2','2: 4 4 | 5 5','3: 4 5 | 5 4','4: "a"','5: "b"','',
          'ababbb','bababa','abbbab','aaabbb','aaaabbb']


def format_input(inputdata):
    rules = {}
    for line in inputdata[:inputdata.index('')]:
        key = line.split(':')[0]
        if line.split(':')[1].replace('"','').strip() in ['a','b']:
            value = line.split(':')[1].replace('"','').strip()
        else:
            value = line.split(':')[1].split('|')
            value = [item.strip().split() for item in value]
        rules[key] = value
    messages = inputdata[inputdata.index('')+1:]
    return rules, messages


def recurse(rule, value, accum, place): 
    for option in rules[rule]:
        for item in option:
            print(rule,option,item,':::',accum,place)
            if item in ['a','b']:
                temp = accum + item
                if temp[:place] == value[:place]:
                    return place + 1, temp
                else:
                    return place, accum
            else:
                place, accum = recurse(item,value,accum,place)
    return place, accum


# adapted from u/MichalMarsalek
def check_rule(text, r, rules):
    if len(text) == 0:
        return []
    if isinstance(rules[r], str):
        if text[0] == rules[r]:
            return [1]
        else:
            return []
    length0 = []
    for disj in rules[r]:
        length = [0]
        for conj in disj:
            length2 = []
            for l in length:
                for c in check_rule(text[l:], conj, rules):                        
                    length2.append(l+c)
            length = length2
        length0.extend(length)         
    return length0


rules, messages = format_input(inputdata)

print(sum(len(q) in check_rule(q,'0',rules) for q in messages))


rules2, messages = format_input(inputdata)
rules2['8'] = [['42'],['42','8']]
rules2['11'] = [['42','31'],['42','11','31']]

print(sum(len(q) in check_rule(q,'0',rules2) for q in messages))
