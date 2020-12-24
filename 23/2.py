import timeit


def get_previous_number(n, cups):
    return (n - 1) if n > 1 else (max(cups))


def main():
    start = timeit.default_timer()
    with open('input.txt') as f: lines = f.readlines()

    cups_list = [ int(x) for x in list(lines[0].strip()) ]

    # Init array
    # Each index it's a value and each value is the next value
    cups = [x + 1 for x in range(0,1000001)]

    for x in range(0, len(cups_list) + 1):
        if x == 0:
            cups[0] = cups_list[0]
        elif (cups_list.index(x) + 1) < len(cups_list):
            cups[x] = cups_list[cups_list.index(x) + 1]
        elif (cups_list.index(x) + 1) == len(cups_list):
            cups[x] = len(cups_list) + 1

    cups[-1] = cups_list[0]




    current = cups[0]
    moves = 10000000

    for move in range(0,moves):
        pickup_start = cups[current]
        pickup_end = cups[cups[cups[current]]]

        # Pick destination
        destination = get_previous_number(current, cups)
        while destination in [pickup_start, cups[pickup_start], pickup_end]:
            destination = get_previous_number(destination, cups)

        # Put pickup cups back and re-wire the array
        cups[current] = cups[pickup_end]
        cups[pickup_end] = cups[destination]
        cups[destination] = pickup_start
        current = cups[current]

    print(cups[1], cups[cups[1]])
    print(cups[1] * cups[cups[1]])

    stop = timeit.default_timer()
    print("Time : %.4f ms" % (1000 * (stop - start)))


if __name__ == '__main__':
    main()
