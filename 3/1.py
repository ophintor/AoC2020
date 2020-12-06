import sys

def main():
    filename = 'input.txt'

    with open(filename) as f:
        lines = f.readlines()

    map = []
    for line in lines:
        map.append(line[:-1])
    width = len(map[0])

    total = 0
    x = 0
    y = 0
    while (x < len(map)):
        # print(x,y)
        # print(map[x])
        # print(map[x][y])
        # print("-" * 80)
        if map[x][y] == "#":
            total += 1
        x += 1
        y = (y+3) % width

    print(total)

if __name__ == '__main__':
    main()
