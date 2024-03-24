import json

with open("data/grid.json", "r") as file:
    grid = json.load(file)

print(grid)

def print_grid(grid):
    for row in grid:
        for cell in row:
            print(cell, end='\t')
            print("", end= "\n")
        print()

print_grid(grid)