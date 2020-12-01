# the report_test function takes a list of integers (report) and adds together combinations in sets of (number) to find a set that adds to the (goal) value
# it returns the sum of the product of the set of integers that sum to the goal value

def report_test(report, number, goal):
    from itertools import combinations  
    report.sort()
    combos = combinations(report, number)
    
    for comb in combos:
        if sum(list(comb)) == goal:
            solution = 1
            for value in comb:
                solution *= value
            return comb, solution
    
    return None