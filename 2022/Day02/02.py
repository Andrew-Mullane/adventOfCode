# Part two

# Rock     A/X 1
# Paper    B/Y 2
# Scissors C/Z 3
# Win  6  Z (A Y,B Z,C X)
# Lose 0  X (A Z,B X,C Y)
# Draw 3  Y (A X,B Y,C Z)

rock = ('A Y','B X','C Z')
paper = ('B Y','A Z','C X')
scissors = ('C Y','A Z','B X')

def winLoseDraw(game: str, total: int):
    if 'X' in game:
        return total + 0
    elif 'Y' in game:
        return total + 3
    elif 'Z' in game:
        return total + 6

def ownHand(game, total):
    if game in rock:
        return total + 1
    elif game in paper:
        return total + 2
    else:
        return total + 3

with open('./input.txt') as f:
    contents = f.readlines()

total: int = 0
for line in contents:
    line = line.rstrip('\n')

    total = ownHand(line, total)
    total = winLoseDraw(line, total)
    # print('-',line)
    # print(total)

print(total)

