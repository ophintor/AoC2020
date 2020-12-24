import timeit
import sys
from math import ceil
from copy import deepcopy

def print_grid(c):
    size = len(c)
    for z in range(size):
        print("z=%d" % ceil(z - (size/2)))
        for x in range(size):
            for y in range(size):
                print(c[z][x][y], end="")
            print("")
        print("")


def init_grid(lines, cycles):
    size = len(lines) + (cycles * 2)
    grid = [[[ '.' for x in range(size) ] for y in range(size) ] for z in range(size) ]
    lines = [ x.strip() for x in lines ]

    z = int(size/2)
    for x in range(cycles, cycles + len(lines)):
        for y in range(cycles, cycles + len(lines)):
            grid[z][x][y] = lines[x - cycles][y - cycles]

    return grid


def find_neighbours(grid,xx,yy,zz):
    size = len(grid)
    neigbours = 0
    for z in range(zz-1,zz+2):
        for x in range(xx-1,xx+2):
            for y in range(yy-1,yy+2):
                if (0 <= x < size) and (0 <= y < size) and (0 <= z < size) and (x != xx or y != yy or z != zz) and (grid[z][x][y] == '#'):
                    neigbours += 1

    return neigbours


def count_active_grids(grid):
    size = len(grid)
    total = 0
    for z in range(size):
        for x in range(size):
            for y in range(size):
                if grid[z][x][y] == '#':
                    total += 1

    return total



def main():
    start = timeit.default_timer()
    with open('input.txt') as f: lines = f.readlines()

    cycles = 6
    grid = init_grid(lines, cycles)
    size = len(grid)

    for cycle in range(0,cycles):
        new_grid = deepcopy(grid)
        for z in range(0,size):
            for x in range(0,size):
                for y in range(0,size):
                    neighbours = find_neighbours(grid,x,y,z)
                    if grid[z][x][y] == "#" and (neighbours < 2 or neighbours > 3):
                        new_grid[z][x][y] = '.'
                    elif grid[z][x][y] == "." and (neighbours == 3):
                        new_grid[z][x][y] = '#'
        grid = new_grid


    active_grids = count_active_grids(new_grid)
    print(active_grids)

    stop = timeit.default_timer()
    print("Time : %.4f ms" % (1000 * (stop - start)))


if __name__ == '__main__':
    main()
