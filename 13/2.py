import sys


def main():
    with open('input.txt') as f:
        lines = f.readlines()

    earliest_time = int(lines[0])
    buses = [ x for x in lines[1][:-1].split(',') ]

    initial_timestamp = int(buses[0])
    timestamp = jump = initial_timestamp

    numbers_only = [ int(x) for x in buses if x != 'x']
    timestamp_limit = 1
    for x in numbers_only:
        timestamp_limit *= x

    found = False
    min_index = 0

    while not found:
        found = True
        for i in range(0, len(buses)):
            if buses[i] != 'x':
                bus = int(buses[i])
                if ((timestamp + i) % bus) != 0:
                    timestamp += jump
                    found = False
                    break

                if (i > min_index):
                    jump = timestamp - initial_timestamp
                    initial_timestamp = timestamp
                    print("Current timestamp %d " % timestamp)
                    print("Jump %d " % jump)
                    min_index = i

    timestamp = timestamp % timestamp_limit
    print("Timestamp: %d" % timestamp)


if __name__ == '__main__':
    main()
