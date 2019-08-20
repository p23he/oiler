import time

# https://projecteuler.net/problem=96

grid = []
for i in range(0, 9):
    grid.append([])
    for j in range(0, 9):
        grid[i].append(0)

def solved_row(grid, i, j):
    temp = []
    for a in range(0, len(grid[i])):
        temp.append(grid[i][a])
    temp[j] = -1
    return grid[i][j] not in temp and 0 not in temp

def choices_row(grid, i, j):
    choices = []
    if grid[i][j] != 0: return choices
    for a in range(1, 10):
        if a not in grid[i]:
            choices.append(a)
    return choices

def solved_col(grid, i, j):
    col = []
    for k in range(0, 9):
        if k == i:
            col.append(-1)
            continue
        col.append(grid[k][j])
    return grid[i][j] not in col and 0 not in col

def choices_col(grid, i, j):
    choices = []
    col = []
    if grid[i][j] != 0: return choices
    for k in range(0, 9):
        col.append(grid[k][j])
    for a in range(1, 10):
        if a not in col:
            choices.append(a)
    return choices

def create_subgrid(grid, a, b, c, d, x, y):
    subgrid = []
    for i in range(a, b):
        for j in range(c, d):
            if i == x and j == y:
                subgrid.append(-1)
                continue
            subgrid.append(grid[i][j])
    return subgrid

def solved_subgrid(grid, i, j):
    subgrid = []
    for a in range(0, 6, 3):
        for b in range(0, 6, 3):
            if a <= i < a + 3 and b <= j < b + 3:
                subgrid = create_subgrid(grid, a, a + 3, b, b + 3, i, j)
    return grid[i][j] not in subgrid and 0 not in subgrid

def choices_subgrid(grid, i, j):
    choices = []
    subgrid = []
    if grid[i][j] != 0: return choices
    for a in range(0, 6, 3):
        for b in range(0, 6, 3):
            if a <= i < a + 3 and b <= j < b + 3:
                subgrid = create_subgrid(grid, a, a + 3, b, b + 3, i, j)
    for a in range(1, 10):
        if a not in subgrid:
            choices.append(a)
    return choices


def solved(grid):
    for i in range(0, 9):
        for j in range(0, 9):
            if not (solved_row(grid, i, j) and solved_col(grid, i, j) and solved_subgrid(grid, i, j)):
                return False
    return True

def choices_cell(grid, i, j):
    if grid[i][j] != 0: return []
    return list(set(choices_row(grid, i, j)).intersection(set(choices_col(grid, i, j)), set(choices_subgrid(grid, i, j))))


def fill_cell(grid, i, j, n):
    if n in choices_cell(grid, i, j):
        grid[i][j] = n
        return grid
    else:
        return 0


def print_grid(grid):
    for i in range(0, 9):
        print(grid[i])
    print()

def solve(grid):
    if solved(grid):
        return True
    else:
        for i in range(0, 9):
            for j in range(0, 9):
                if grid[i][j] == 0:
                    choices = choices_cell(grid, i, j)
                    if not choices: return False
                    for c in range(0, len(choices)):
                        grid[i][j] = choices[c]
                        if solve(grid):
                            return True
                        grid[i][j] = 0
                    return False

total = 0
f = open('sudoku.txt', 'r')
for x in f:
    print(x)
    if 'Grid' in x:
        grid = []
        for i in range(0, 9):
            line = f.readline()
            if '\n' in line: line = line[:-1]
            grid.append(list(map(int, list(line))))
        solve(grid)
        num = str(grid[0][0]) + str(grid[0][1]) + str(grid[0][2])
        total += int(num)
print(total)
