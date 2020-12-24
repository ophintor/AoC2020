import sys


def check_buses(time, buses):
    found = False
    for bus in buses:
        print ("checking bus %d at %d" % (bus, time))
        if time % bus == 0:
            found = True
            break

    return (found, bus)


def main():
    with open('input.txt') as f:
        lines = f.readlines()

    earliest_time = int(lines[0])
    buses = [ int(x) for x in lines[1][:-1].split(',') if x != 'x']

    print(earliest_time)
    print(buses)

    bus_found = False
    current_time = earliest_time

    while not bus_found:
        bus_found, bus = check_buses(current_time, buses)
        if not bus_found:
            current_time += 1

    print ((current_time - earliest_time) * bus)


if __name__ == '__main__':
    main()
