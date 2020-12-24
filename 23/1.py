import timeit

def print_cups(cups, current):
    for cup in cups:
        print("(", cup, ")", end = '  ') if cup == current else print(cup, end = '  ')
    print()

def get_previous_number(n, cups):
    return (n - 1) if n > 1 else max(cups)

def turn_around_cups(cups, i1, i2):
    diff = i1 - i2
    index = diff % len(cups)
    cups = cups[-index:] + cups[:-index]
    return cups

def main():
    start = timeit.default_timer()
    with open('input.txt') as f: lines = f.readlines()

    cups = [ int(x) for x in list(lines[0].strip()) ]
    current = cups[0]
    size = len(cups)
    moves = 100

    while moves > 0:
        current_index = cups.index(current)

        # Pick up cups
        pickup = cups[current_index+1:current_index+4]
        del cups[current_index+1:current_index+4]
        missing = 3 - len(pickup)
        if missing > 0:
            pickup += cups[0:missing]
            del cups[0:missing]

        # Pick destination
        destination = get_previous_number(current, cups)
        while destination in pickup:
            destination = get_previous_number(destination, cups)

        destination_index = cups.index(destination)

        # Put pick up cups back
        for i in range(len(pickup)):
            cups.insert(destination_index + i + 1, pickup[i])

        cups = turn_around_cups(cups, current_index, cups.index(current))

        current = cups[(current_index + 1) % size]
        moves -= 1

    # Get the solution
    cups = turn_around_cups(cups, 0, cups.index(1))[1:]
    for i in cups:
        print(i, end='')
    print()

    stop = timeit.default_timer()
    print("Time : %.4f ms" % (1000 * (stop - start)))


if __name__ == '__main__':
    main()
