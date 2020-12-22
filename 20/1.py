import timeit
import re
import math


def get_top_side(tile):
    return tile[0]

def get_top_side_flipped(tile):
    return tile[0][::-1]

def get_right_side(tile):
    return ''.join([x[-1] for x in tile])

def get_right_side_flipped(tile):
    return ''.join([x[-1] for x in tile[::-1]])

def get_bottom_side(tile):
    return tile[-1]

def get_bottom_side_flipped(tile):
    return tile[-1][::-1]

def get_left_side(tile):
    return ''.join([x[0] for x in tile])

def get_left_side_flipped(tile):
    return ''.join([x[0] for x in tile[::-1]])

def get_number_of_matching_sides(tile1, tile2):
    tile1_sides = [ get_left_side(tile1), get_right_side(tile1), get_top_side(tile1), get_bottom_side(tile1) ]
    tile2_sides = [ get_left_side(tile2), get_left_side_flipped(tile2), get_right_side(tile2), get_right_side_flipped(tile2),
                    get_top_side(tile2), get_bottom_side(tile2), get_top_side_flipped(tile2), get_bottom_side_flipped(tile2) ]

    return len(set(tile1_sides) & set(tile2_sides))


def main():
    start = timeit.default_timer()
    with open('input.txt') as f: lines = f.read()

    tiles_list = lines.split('\n\n')
    tiles = {}
    corners = []

    for t in tiles_list:
        tiles[int(re.search(r'\d+', t)[0])] = t.split(':')[1].strip().split('\n')

    for tk in tiles.keys():
        m = 0
        for tk_to_match in tiles.keys():
            if tk != tk_to_match:
                m += get_number_of_matching_sides(tiles[tk], tiles[tk_to_match])
        if m == 2:
            corners.append(tk)

    solution = 1
    for value in corners:
        solution *= value

    print(solution)

    stop = timeit.default_timer()
    print("Time : %.4f ms" % (1000 * (stop - start)))


if __name__ == '__main__':
    main()
