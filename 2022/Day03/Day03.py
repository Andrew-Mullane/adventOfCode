
def get_compartments(line: str) -> list[set]:
    # getting compartments
    return [set(line[:len(line) // 2]), set(line[len(line) // 2:])]

def get_compartment_intersect(compartments: list[set]) -> str:
    # getting common items
    return list(set.intersection(*compartments))[0]

def char_to_priority(char: str):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38

def solution1() -> int:
    file = open('./input.txt', 'r')
    return sum(
        [char_to_priority(
            get_compartment_intersect(
                get_compartments(line)
            )
        )
            for line in file
        ]
    )
print(solution1())


def solution2() -> int:
    lines = open('./input.txt', 'r').readlines()
    score = 0
    for i in range(0,len(lines), 3):
        curr_group = [set(el.strip('\n')) for el in lines[i:i + 3]]
        score += char_to_priority(get_compartment_intersect(curr_group))
    
    return score  
    
print(solution2())