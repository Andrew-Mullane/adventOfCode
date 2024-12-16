# look up the problem
file = open("input.txt", "r")
values = file.readlines()


def lists(vals):
    listA = []
    listB = []
    for i in vals:
        listA.append(int(i.split()[0]))
        listB.append(int(i.split()[1]))
    listA.sort()
    listB.sort()
    # Organise input into 2 lists and sort
    return listA, listB
        
def delta(a,b):
    deltas = []
    for i in range(len(a)):
        deltas.append(abs(a[i] - b[i]))
    # find differences between numbers on each list
    return deltas
  
def part_one(values):
    first, second = lists(values)

    distances = delta(first,second)

    total_distance = sum(distances)
    # sum total difference numbers
    return total_distance

def sim_score(a,b):
    score = 0
    for i in a:
        if i in b:
            inst = b.count(i)
            score += inst * i
    # check instances of list A values in list B and multiply
    return score

def part_two(values):
    first, second = lists(values)
    
    similarity = sim_score(first,second)

    return similarity


print(part_one(values))
print(part_two(values))
