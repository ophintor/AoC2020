import sys

def main():
    filename = 'input.txt'

    with open(filename) as f:
        lines = f.readlines()

    map = []
    for line in lines:
        map.append(line[:-1])
    width = len(map[0])

    total=1
    routes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    for right,down in routes:
        x = 0
        y = 0
        # print (right,down)
        trees = 0
        while (x < len(map)):
            # print(x,y)
            # print(map[x])
            # print(map[x][y])
            # print("-" * 80)
            if map[x][y] == "#":
                trees += 1
            x += down
            y = (y+right) % width

        # print(trees)
        total *= trees

    print(total)

if __name__ == '__main__':
    main()
