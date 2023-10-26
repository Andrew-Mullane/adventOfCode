

def parse_input(file):
    levels, instructions = [section.split('\n') for section in file.read().split('\n\n')]
    levels = [crate.replace('    ', ' [X] ') for crate in levels[:-1]]
    levels = [[crate[1] for crate in level.split()] for level in levels]
    stacks = [[] for _ in range(len(levels[0]))]
    for level in reversed(levels):
        for index, crate in enumerate(level):
            if crate != "X":
                stacks[index].append(crate)

    return instructions, levels, stacks

def task1(file):
    instructions,levels,stacks = parse_input(file)
    for instruction in instructions:
        quantity,from_stack,to_stack = [int(i) for i in instruction.split() if i.isnumeric()]
        while quantity != 0:
            stacks[to_stack-1].append(stacks[from_stack-1].pop())
            quantity -= 1
    top_level = ""
    for stack in stacks:
        top_level += str(stack[-1])
    print("Task 1 top level: " + top_level)

def task2(file):
    instructions,levels,stacks = parse_input(file)
    for instruction in instructions:
        quantity,from_stack,to_stack = [int(i) for i in instruction.split() if i.isnumeric()]
        stacks[to_stack-1].extend(stacks[from_stack-1][-quantity:])
        del stacks[from_stack-1][-quantity:]
    top_level = ""
    for stack in stacks:
        top_level += str(stack[-1])
    print("Task 2 top level: " + top_level)

def main():
    print("AoC Day 05:")
    task1_input = open('./input.txt', 'r')
    task2_input = open('./input.txt', 'r')
    task1(task1_input)
    task2(task2_input)

if __name__ == "__main__":
    main()
