# input
def read_input():
    with open('./input.txt', 'r') as f:
        puzzle_input = f.read().strip().splitlines()
    return [list(row) for row in puzzle_input]

def word_search(grid):
    keyword = "XMAS"
    target_length = len(keyword)
    count = 0
    rows = len(grid)
    cols = len(grid[0])

    def is_valid_direction(row, col, dr, dc):
        for i in range(target_length):
            r = row + i * dr
            c = col + i * dc
            if not (0 <= r < rows and 0 <= c < cols) or grid[r][c]!= keyword[i]:
                return False
        return True
    
    for row in range(rows):
        for col in range(cols):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
            for dr, dc in directions:
                if is_valid_direction(row, col, dr, dc):
                    count += 1
    return count

def part_one():
    grid = read_input()
    print(word_search(grid))



def X_search(grid):
    keyword = "A"
    count = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for row in range(rows):
        for col in range(cols):
            directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
            if grid[row][col] == "A":
                for dr, dc in directions:
                    checkX(row, col, dr, dc)
                    
    return count
