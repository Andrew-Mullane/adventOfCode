def get_pairs(line: str) -> list[str]:
    return line.rstrip().split(',')

def split_pairs(pairs: list) -> list:
    return [pair.split('-') for pair in pairs]

def pairs_to_ints(pairs:list) -> list:
    return list(map(lambda x: list(map(int, x)), pairs))

def pairs_to_ranges(pairs:list) -> list:
    first = range(pairs[0][0],(pairs[0][1]+1))
    second = range(pairs[1][0],(pairs[1][1]+1))
    return [[*first],[*second]]

def check_pairs_shared(pairs:list) -> int:
    if set(pairs[0]).issubset(pairs[1]):
        return 1
    elif set(pairs[1]).issubset(pairs[0]):
        return 1
    else:
        return 0

def check_pairs_intersect(pairs:list) -> int:
    if set(pairs[0]).intersection(pairs[1]):
        return 1
    elif set(pairs[1]).intersection(pairs[0]):
        return 1
    else:
        return 0

file = open('./input.txt', 'r')
lines = file.readlines()
# lines = ["2-3,1-5","4-9,5-7"]
def solution1(pairs:list) -> int:
    return sum(check_pairs_shared(
        pairs_to_ranges(
            pairs_to_ints(
                split_pairs(
                    get_pairs(line)
                )
            )
        )
    )
    for line in lines)

# print(solution1(lines))

def solution2(pairs:list) -> list:
    return sum(check_pairs_intersect(
        pairs_to_ranges(
            pairs_to_ints(
                split_pairs(
                    get_pairs(line)
                )
            )
        )
    )
    for line in lines)

print(solution2(lines))

