
# Rock     A/X 1
# Paper    B/Y 2
# Scissors C/Z 3
# Win  6  Z (A Y,B Z,C X)
# Lose 0  X (A Z,B X,C Y)
# Draw 3  Y (A X,B Y,C Z)

win  = ('A Y','B Z','C X')
lose = ('A Z','B X','C Y')
draw = ('A X','B Y','C Z')

def ownHand(game: str, total: int):
    if 'X' in game:
        return total + 1
    elif 'Y' in game:
        return total + 2
    elif 'Z' in game:
        return total + 3

def winLoseDraw(game, total):
    if game in win:
        return total + 6
    elif game in draw:
        return total + 3
    else:
        return total + 0

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

