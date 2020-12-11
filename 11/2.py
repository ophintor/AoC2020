import sys


def show_data(data):
    for line in data:
        print(''.join(line))
    print("")


def check_seat(data, i, j):
    if data[i][j] == '#':
        occupied = 1
        found = True
    elif data[i][j] == 'L':
        occupied = 0
        found = True
    else:
        occupied = 0
        found = False

    return occupied, found


def is_top_left_occupied(data,i,j):
    found = False
    occupied = 0
    while (i >= 0) and (j >= 0) and (not found):
        occupied, found = check_seat(data, i, j)
        i -= 1
        j -= 1

    return occupied


def is_top_occupied(data,i,j):
    found = False
    occupied = 0
    while (j >= 0) and (not found):
        occupied, found = check_seat(data, i, j)
        j -= 1

    return occupied


def is_top_right_occupied(data,i,j):
    found = False
    occupied = 0
    while (i < len(data)) and (j >= 0) and (not found):
        occupied, found = check_seat(data, i, j)
        i += 1
        j -= 1

    return occupied


def is_right_occupied(data,i,j):
    found = False
    occupied = 0
    while (i < len(data)) and (not found):
        occupied, found = check_seat(data, i, j)
        i += 1

    return occupied


def is_bottom_right_occupied(data,i,j):
    found = False
    occupied = 0
    while (i < len(data)) and (j < len(data[i])) and (not found):
        occupied, found = check_seat(data, i, j)
        i += 1
        j += 1

    return occupied


def is_bottom_occupied(data,i,j):
    found = False
    occupied = 0
    while (j < len(data[0])) and (not found):
        occupied, found = check_seat(data, i, j)
        j += 1

    return occupied


def is_bottom_left_occupied(data,i,j):
    found = False
    occupied = 0
    while (i >= 0) and (j < len(data[i])) and (not found):
        occupied, found = check_seat(data, i, j)
        i -= 1
        j += 1

    return occupied


def is_left_occupied(data,i,j):
    found = False
    occupied = 0
    while (i >= 0) and (not found):
        occupied, found = check_seat(data, i, j)
        i -= 1

    return occupied


def get_occupied_seats(data,i,j):
    occupied_seats = (  is_top_left_occupied(data, i-1, j-1) +
                        is_top_occupied(data, i, j-1) +
                        is_top_right_occupied(data, i+1, j-1) +
                        is_right_occupied(data, i+1, j) +
                        is_bottom_right_occupied(data, i+1, j+1) +
                        is_bottom_occupied(data, i, j+1) +
                        is_bottom_left_occupied(data, i-1, j+1) +
                        is_left_occupied(data, i-1, j) )

    # print(occupied_seats)
    return occupied_seats


def count_seats(data):
    seats = 0
    for line in data:
        for x in line:
            if x == "#": seats += 1

    return seats


def main():
    with open('input.txt') as f:
        lines = f.readlines()

    data = [[char for char in line[:-1]] for line in lines]
    data_next = [['.' for char in line[:-1]] for line in lines]

    end = False
    round = 1
    while not end:
        for i in range(0,len(data)):
            for j in range(0,len(data[i])):
                if (data[i][j] == 'L') and (get_occupied_seats(data,i,j) == 0):
                    data_next[i][j] = '#'
                elif (data[i][j] == '#') and (get_occupied_seats(data,i,j) >= 5):
                    data_next[i][j] = 'L'

        print ("Round %d" % round)
        round += 1
        if data == data_next:
            seats = count_seats(data)
            print(seats)
            end = True
        else:
            data = [x[:] for x in data_next]


if __name__ == '__main__':
    main()
