import sys
import math


def calculate_row(row):
    min = 0
    max = 127
    for i in range(0,len(row)):
        if row[i] == "F":
            max = max - math.ceil((max - min)/2)
        elif row[i] == "B":
            min = min + math.ceil((max - min)/2)

    return min


def calculate_seat(seat):
    min = 0
    max = 7
    for i in range(0,len(seat)):
        if seat[i] == "L":
            max = max - math.ceil((max - min)/2)
        elif seat[i] == "R":
            min = min + math.ceil((max - min)/2)

    return min


def find_my_seat(seats):
    for i in range(0,len(seats)):
        if (seats[i] + 1) != (seats[i+1]):
            seat = seats[i] + 1
            break

    return seat


def main():
    filename = 'input.txt'
    seats = []
    max_seat = 0

    with open(filename) as f:
        lines = f.readlines()

    for line in lines:
        row  = line[0:7]
        seat = line[7:10]
        seat_number = (calculate_row(row) * 8) + calculate_seat(seat)
        seats.append(seat_number)

    seats.sort()
    seat = find_my_seat(seats)
    print(seat)


if __name__ == '__main__':
    main()
