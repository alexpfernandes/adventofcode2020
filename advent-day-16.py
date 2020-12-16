# This will open a text file, split it into a list of each line
file = open('advent-day-16.txt',newline='')
inputdata = file.read().splitlines()
sample = ['class: 1-3 or 5-7','row: 6-11 or 33-44','seat: 13-40 or 45-50','',
          'your ticket:','7,1,14','','nearby tickets:','7,3,47','40,4,50','55,2,20','38,6,12']
sample2 = ['class: 0-1 or 4-19','row: 0-5 or 8-19','seat: 0-13 or 16-19','',
           'your ticket:','11,12,13','','nearby tickets:','3,9,18','15,1,5','5,14,9']


# This splits the input into three variables:
# A rules dictionary, a list of values for my ticket, and a list of lists of values for nearby tickets
def input_parser(info):
    section = 0
    rules, my_ticket, nearby_tickets = {}, [], []
    for line in info:
        if line == '' or line[-1] == ':':
            section += 1
        elif section == 0:
            rule = line.split(':')
            values = [i.strip().split('-') for i in rule[1].split('or')]
            values = [[int(i) for i in pair] for pair in values]
            rules[rule[0]] = values
        elif section == 2:
            my_ticket.append([int(num) for num in line.split(',')])
        elif section == 4:
            nearby_tickets.append([int(num) for num in line.split(',')])
    return rules, my_ticket, nearby_tickets


# This function creates a list of all of the invalid numbers within each ticket,
# that is, numbers which couldn't possibly satisfy any rule
def invalid_counter(rules, tickets):
    invalid_nums = []
    for ticket in tickets:
        for value in ticket:
            validnum = False
            for rule in rules.values():
                if rule[0][0] <= value <= rule[0][1] or rule[1][0] <= value <= rule[1][1]:
                    validnum = True
                    break
            if validnum == False:
                invalid_nums.append(value)
    return invalid_nums


# Solution to Part 1
rules, my_ticket, nearby_tickets = input_parser(inputdata)
sum(invalid_counter(rules, nearby_tickets))


# This function returns a list of valid tickets
# by checking each value against the list of rules and ensuring that it can pass at least one rule
def ticket_validator(rules, tickets):
    valid_tickets = []
    for ticket in tickets:
        for value in ticket:
            validnum = False
            for rule in rules.values():
                if rule[0][0] <= value <= rule[0][1] or rule[1][0] <= value <= rule[1][1]:
                    validnum = True
                    break
            if validnum == False:
                break
        else:
            valid_tickets.append(ticket)
    return valid_tickets


# This function solves the logic puzzle of which index in the list of ticket values corresponds to which rule
# It works by looping through a transposed list of the ticket values,
# that is, the first element of each ticket, then the second, etc.
# it checks to see if there is only 1 valid rule that satisfies all inputs
# if one exists, it crosses that rule and column of values of the list and continues
# it will iterate until every rule has been exhausted
# This is a really clunky solution, and uses what must be a ton of bad practices,
# especially when it deletes rules out of the copied rule list.
def rule_identifier(rules,valid_tickets):
    from copy import deepcopy
    values = list(zip(*valid_tickets))
    rules_order = ['' for i in range(20)]
    temp_rules = deepcopy(rules)
    while len(temp_rules) > 0:    
        del_fields = []
        for index,field in enumerate(values):
            if field == 'used':
                continue
            else:
                valid_rules = deepcopy(temp_rules)
                for num in field:
                    del_rules = []
                    for key,rule in valid_rules.items():
                        if rule[0][0] <= num <= rule[0][1] or rule[1][0] <= num <= rule[1][1]:
                            pass
                        else:
                            del_rules.append(key)
                    for key in del_rules:
                        del valid_rules[key]
                    if len(valid_rules) == 1:
                        name = list(valid_rules.keys())[0]
                        rules_order[index] = name
                        del temp_rules[name]
                        del_fields.append(index)
                        break
        for index in del_fields:
            values[index] = 'used'
    return rules_order


# This applies the rules in the appropriate order and finds the cumulative product for each 'departure' field
def ticket_value(ticket,rules_order):
    product = 1
    for index, rule in enumerate(rules_order):
        if rule[:3] == 'dep':
            product *= my_ticket[0][index]
    return product


# Solution to Part 2
rules, my_ticket, nearby_tickets = input_parser(inputdata)
valid_tickets = ticket_validator(rules,nearby_tickets)
rules_order = rule_identifier(rules, valid_tickets)
ticket_value(my_ticket, rules_order)
