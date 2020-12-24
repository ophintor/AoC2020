import sys

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    data = [line[:-1] for line in lines]

    # N, E, S, W
    coords = [0, 0, 0, 0]
    waypoint = [1, 10, 0, 0]

    for action in data:
        direction = action[0]
        distance  = int(action[1:])

        # print("%s %d " % (direction, distance))

        if direction == "F":
            for i in range(0, len(coords)):
                coords[i] += distance * waypoint[i]
        elif direction == "R" or direction == "L":
            wp_copy = [ i for i in waypoint ]
            for i in range(0, len(waypoint)):
                positions = int(distance / 90)
                if direction == "R":
                    waypoint[i] = wp_copy[(i - positions) % len(waypoint)]
                elif direction == "L":
                    waypoint[i] = wp_copy[(i + positions) % len(waypoint)]
        elif direction == "N":
            waypoint[0] += distance
        elif direction == "E":
            waypoint[1] += distance
        elif direction == "S":
            waypoint[2] += distance
        elif direction == "W":
            waypoint[3] += distance

    print(abs(coords[0]-coords[2]) + abs(coords[1]-coords[3]))


if __name__ == '__main__':
    main()
