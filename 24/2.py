import timeit


def is_tile_white(grid, coords):
    return coords not in grid or grid[coords] == 0


def is_tile_black(grid, coords):
    return coords in grid and grid[coords] == 1


def black_tiles_around(grid, x, y):
    count = 0
    if is_tile_black(grid, (x, y+1)):   count += 1
    if is_tile_black(grid, (x+1, y)):   count += 1
    if is_tile_black(grid, (x+1, y-1)): count += 1
    if is_tile_black(grid, (x, y-1)):   count += 1
    if is_tile_black(grid, (x-1, y)):   count += 1
    if is_tile_black(grid, (x-1, y+1)): count += 1
    return count


def flip_one_tile(grid, coords):
    grid[coords] = abs(grid[coords] - 1) if coords in grid.keys() else 1
    return grid


def flip_tiles(grid):
    tiles_range = { "min" : [0,0], "max" : [0,0] }
    next_grid = dict(grid)

    for coords in grid.keys():
        for i in range(2):
            if list(coords)[i] < tiles_range["min"][i]: tiles_range["min"][i] = list(coords)[i]
            if list(coords)[i] > tiles_range["max"][i]: tiles_range["max"][i] = list(coords)[i]

    for x in range(tiles_range["min"][0] - 1, tiles_range["max"][0] + 2):
        for y in range(tiles_range["min"][1] - 1, tiles_range["max"][1] + 2):
            if is_tile_white(grid, (x,y)) and black_tiles_around(grid, x, y) == 2:
                next_grid = flip_one_tile(next_grid, (x,y))
            elif is_tile_black(grid, (x,y)) and (black_tiles_around(grid, x, y) == 0 or black_tiles_around(grid, x, y) > 2):
                next_grid = flip_one_tile(next_grid, (x,y))

    return next_grid


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
    days = 100

    for directions in lines:
        coords = find_tile_coords(directions.strip())
        grid = flip_one_tile(grid, coords)

    for i in range(days):
        grid = flip_tiles(grid)

    print(list(grid.values()).count(1))

    stop = timeit.default_timer()
    print("Time : %.4f ms" % (1000 * (stop - start)))


if __name__ == '__main__':
    main()
