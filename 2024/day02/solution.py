# load data in
file = open("input.txt", "r")
values = file.readlines()

sample =["7 6 4 2 1"
        ,"1 2 7 8 9"
        ,"9 7 6 2 1"
        ,"1 3 2 4 5"
        ,"8 6 4 4 1"
        ,"1 3 6 7 9"]

# print(values[0])
def input_to_lists(vals):
    reports = []
    for i in vals:
        reports.append([int(x) for x in i.split()])
    return reports

def sign(num):
    if num < 0:
        return -1
    elif num > 0:
        return 1
    else:
        return 0

def isSafe(report):
    expectedSign = sign(report[1] - report[0])
    for i in range(1,len(report)):
        delta = report[i] - report[i-1]
        if sign(delta) != expectedSign:
            return False
        elif abs(delta) < 1:
            return False
        elif abs(delta) > 3:
            return False
    return True

def scanReport(report):
    for i in range(len(report)):
        newReport = report.copy()
        newReport.pop(i)
        # print(newReport)
        if isSafe(newReport):
            return True

        
def part_one(values):
    reports = input_to_lists(values)
    safe_scores = 0
    for report in reports:
        if isSafe(report):
            safe_scores += 1
    return safe_scores
        
        
def part_two(values):
    reports = input_to_lists(values)
    safe_scores = 0
    for report in reports:
        if scanReport(report):
            safe_scores += 1
    return safe_scores

        
print(part_one(values))
print(part_two(values))
