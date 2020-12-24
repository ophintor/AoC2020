import timeit


def flip_one_tile(grid, coords):
    grid[coords] = abs(grid[coords] - 1) if coords in grid.keys() else 1
    return grid


def find_tile_coords(directions):
    i = 0
    dir_set = ('e', 'se', 'sw', 'w', 'nw', 'ne')
    coords = (0, 0)

    while i < len(directions):
        if directions[i:i+2] in dir_set and directions[i:i+2] == 'se':
            coords = ( coords[0] + 1, coords[1] - 1 )
            i += 2
        elif directions[i:i+2] in dir_set and directions[i:i+2] == 'sw':
            coords = ( coords[0], coords[1] - 1 )
            i += 2
        elif directions[i:i+2] in dir_set and directions[i:i+2] == 'nw':
            coords = ( coords[0] - 1, coords[1] + 1 )
            i += 2
        elif directions[i:i+2] in dir_set and directions[i:i+2] == 'ne':
            coords = ( coords[0], coords[1] + 1 )
            i += 2
        elif directions[i] in dir_set and directions[i] == 'e':
            coords = ( coords[0] + 1, coords[1] )
            i += 1
        elif directions[i] in dir_set and directions[i] == 'w':
            coords = ( coords[0] - 1, coords[1] )
            i += 1

    return coords


def main():
    start = timeit.default_timer()
    with open('input.txt') as f: lines = f.readlines()

    grid = {}

    for directions in lines:
        coords = find_tile_coords(directions.strip())
        grid = flip_one_tile(grid, coords)

    print(list(grid.values()).count(1))

    stop = timeit.default_timer()
    print("Time : %.4f ms" % (1000 * (stop - start)))


if __name__ == '__main__':
    main()
