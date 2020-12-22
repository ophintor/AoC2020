import timeit
import re
from math import sqrt


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

def rotate_tile(tile):
    x = list(zip(*tile[::-1]))
    return [''.join(i) for i in x]

def flip_tile(tile):
    for i in range(len(tile)):
        tile[i] = tile[i][::-1]
    return tile

def is_horizontal_match(tile_left, tile_right):
    return get_right_side(tile_left) == get_left_side(tile_right)

def is_vertical_match(tile_top, tile_bottom):
    return get_bottom_side(tile_top) == get_top_side(tile_bottom)

def print_tile(tile):
    for t in tile:
        print(t)

def print_image(tiles, image):
    size = int(sqrt(len(tiles)))
    tile_size = len(tiles[image[0]][0])

    for x in range(size):
        for y in range(tile_size):
            for z in range(size):
                print(tiles[image[(z % size) + (x * size)]][y % tile_size], end = " ")
            print(" ")
        print()

def create_image_from_tiles(tiles, image):
    size = int(sqrt(len(tiles)))
    tile_size = len(tiles[image[0]][0])
    single_image = []

    for x in range(size):
        for y in range(tile_size):
            single_image.append("")
            for z in range(size):
                single_image[-1] += tiles[image[(z % size) + (x * size)]][y % tile_size]

    # print_tile(single_image)
    return single_image

def create_monster():
    monster = []
    monster.append("                  # ")
    monster.append("#    ##    ##    ###")
    monster.append(" #  #  #  #  #  #   ")

    return monster

def check_monster_on_coords(image, monster, x, y):
    match = True

    for i in range(x, x + len(monster)):
        for j in range(y, y + len(monster[0])):
            if ((i >= len(image[0]) or j>= len(image)) or
                (monster[i - x][j - y] == '#' and image[i][j] != '#')):
                match = False
                break

    if match:
        for i in range(len(image)):
            image[i] = list(image[i])

        for i in range(x, x + len(monster)):
            for j in range(y, y + len(monster[0])):
                if (monster[i - x][j - y] == '#' and image[i][j] == '#'):
                    image[i][j] = "0"

    return match


def find_monsters(single_image):
    found = False
    monsters = 0
    counter = 8
    hashes = 0
    monster = create_monster()

    while not found and counter > 0:
        if counter % 4:
            flip_tile(monster)
        else:
            rotate_tile(monster)

        for x in range(0, len(single_image[0])):
            for y in range(0, len(single_image)):
                is_a_match = check_monster_on_coords(single_image, monster, x, y)
                if is_a_match:
                    found = True
                    monsters += 1
                    # hashes = 0
                    # for i in range(len(single_image)):
                    #     hashes += single_image[i].count('#')

        counter -= 1

    for i in range(len(single_image)):
        hashes += single_image[i].count('#')

    print("Found %d monsters and %d hashes" % ( monsters, hashes))


def can_tile_squeeze_here(tiles, tk, image, position):
    size = int(sqrt(len(tiles)))
    pos_top = position - size
    pos_left = position - 1
    it_fits = False

    if position == 0:
        it_fits = True

    elif position == 1:
        rotations_current = 4
        rotations_neighbour = 4
        flips = 4

        for fl in range(flips):
            for rc in range(rotations_current):
                for rn in range(rotations_neighbour):
                    if is_horizontal_match(tiles[image[pos_left]], tiles[tk]):
                        return True
                    else:
                        tiles[image[pos_left]] = rotate_tile(tiles[image[pos_left]])

                if is_horizontal_match(tiles[image[pos_left]], tiles[tk]):
                    return True
                else:
                    tiles[tk] = rotate_tile(tiles[tk])

            if is_horizontal_match(tiles[image[pos_left]], tiles[tk]):
                return True
            elif fl % 2 == 0:
                tiles[tk] = flip_tile(tiles[tk])
            elif fl % 2 == 1:
                tiles[image[pos_left]] = flip_tile(tiles[image[pos_left]])

    else:
        rotations_current = 4
        flips = 2
        possible_positions = rotations_current * flips

        while not it_fits and possible_positions > 0:

            if ((pos_top < 0 and is_horizontal_match(tiles[image[pos_left]], tiles[tk])) or
                (position % size == 0 and is_vertical_match(tiles[image[pos_top]], tiles[tk]) or
                (pos_top > 0 and is_vertical_match(tiles[image[pos_top]], tiles[tk])) and is_horizontal_match(tiles[image[pos_left]], tiles[tk]))):
                    it_fits = True
            elif possible_positions % 4 == 0:
                tiles[tk] = flip_tile(tiles[tk])
            else:
                tiles[tk] = rotate_tile(tiles[tk])

            possible_positions -= 1

    return it_fits


def does_this_tile_go_in_a_corner(position, size):
    return (position == (size - size) or
            position == (size - 1) or
            position == ((size * size) - size) or
            position == ((size * size) - 1))


def sort_tiles(image, corners, tiles, position, used):
    size = sqrt(len(tiles))

    if (len(image) < len(tiles)):
        for tk in tiles.keys():
            if tk not in image and tk not in used[position] and can_tile_squeeze_here(tiles, tk, image, position):
                if ((does_this_tile_go_in_a_corner(position, size) and tk in corners) or
                    (not does_this_tile_go_in_a_corner(position, size) and not tk in corners)):
                    image.append(tk)
                    used[position].append(tk)
                    sort_tiles(image, corners, tiles, position + 1, used)

        if (len(image) < len(tiles) and position > 0):
            image.pop()
            position -= 1
            used[position] = []


def main():
    start = timeit.default_timer()
    with open('input.txt') as f: lines = f.read()

    tiles_list = lines.split('\n\n')
    tiles = {}
    used = {}
    corners = []
    image = []
    count = 0

    for t in tiles_list:
        tiles[int(re.search(r'\d+', t)[0])] = t.split(':')[1].strip().split('\n')

    for tk in tiles.keys():
        m = 0
        for tk_to_match in tiles.keys():
            if tk != tk_to_match:
                m += get_number_of_matching_sides(tiles[tk], tiles[tk_to_match])
        if m == 2:
            corners.append(tk)

    for i in range(len(tiles)):
        used[i] = []

    sort_tiles(image, corners, tiles, 0, used)

    for t in tiles.keys():
        tiles[t] = tiles[t][1:-1]
        for x in range(len(tiles[t])):
            tiles[t][x] = tiles[t][x][1:-1]

    find_monsters(create_image_from_tiles(tiles, image))

    stop = timeit.default_timer()
    print("Time : %.4f ms" % (1000 * (stop - start)))


if __name__ == '__main__':
    main()
