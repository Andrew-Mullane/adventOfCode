# look up the problem
file = open("input.txt", "r")
values = file.readlines()


sum = 0
def part1(values):
    for i in values:
        coords = []
        for k in i:
            if k.isdigit():
                coords.append(k)
        value = int(coords[0] + coords[-1])
        sum += value
    return sum
    print(sum)

def part2(values):
    
