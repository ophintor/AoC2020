import sys

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    data = [line[:-1] for line in lines]

    coords = [0,0]
    facing = "E"
    coords_degrees = {
        "N" : 0,
        "E" : 90,
        "S" : 180,
        "W" : 270
    }
    coords_degrees_keys = list(coords_degrees.keys())
    coords_degrees_vals = list(coords_degrees.values())

    for action in data:
        direction = action[0]
        distance  = int(action[1:])

        print("%s %d " % (direction, distance))

        if direction == "F":
            direction = facing
        elif direction == "R":
            facing = coords_degrees_keys[coords_degrees_vals.index((coords_degrees[facing] + distance) % 360)]
            print("Turning to the %s" % facing)
        elif direction == "L":
            facing = coords_degrees_keys[coords_degrees_vals.index((coords_degrees[facing] - distance) % 360)]
            print("Turning to the %s" % facing)

        if direction == "N":
            coords[1] += distance
            print("Going %s %d " % (direction, distance))
        elif direction == "E":
            coords[0] += distance
            print("Going %s %d " % (direction, distance))
        elif direction == "S":
            coords[1] -= distance
            print("Going %s %d " % (direction, distance))
        elif direction == "W":
            coords[0] -= distance
            print("Going %s %d " % (direction, distance))

        print(coords)
        print(" ")

    print(abs(coords[0]) + abs(coords[1]))


if __name__ == '__main__':
    main()
