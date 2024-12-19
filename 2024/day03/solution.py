import re

# load data in
file = open("input.txt", "r")
values = file.readlines()
values = "".join(values)
file.close()

test_line = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

test_line2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

do_str = r"do\(\)"
dont_str = r"don't\(\)"

def clear_dont(memory):
    a = re.split(dont_str, memory)
    do_blocks = [a[0]]
    for i in a[1:]:
        if re.search(do_str, i):
            line = re.split(do_str, i)
            for block in line[1:]:
                do_blocks.append(block)
    return do_blocks

def clean(memory):
    matches = re.findall(r"mul\(\d+,\d+\)", memory)
    return matches

def strip_operator(ops):
    digits = []
    for op in ops:
        digits.append([int(x) for x in re.findall(r"\d+",op)])
    return digits

def add_up(vals):
    total = 0
    for val in vals:
        total += val[0] * val[1]
    return total

def part_one(values):
    uncorrupted = clean(values)
    values = strip_operator(uncorrupted)
    total = add_up(values)
    print(total)

def part_two(values):
    test = clear_dont(values)
    do_values = "".join(test)
    uncorrupted = clean(do_values)
    values = strip_operator(uncorrupted)
    total = add_up(values)
    print(total)

part_one(values)
part_two(values)