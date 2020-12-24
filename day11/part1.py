import sys


def show_data(data):
    for line in data:
        print(''.join(line))
    print("")


def get_occupied_seats(data,i,j):
    occupied_seats = 0
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if ((x != i) or (y != j)) and (x >= 0) and (y >= 0) and (x < len(data)) and (y < len(data[i])):
                if (data[x][y] == '#'):
                    occupied_seats += 1

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
                elif (data[i][j] == '#') and (get_occupied_seats(data,i,j) >= 4):
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
