import sys

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    data = [int(line) for line in lines]
    data.append(0)
    data.sort()
    data.append(data[len(data) - 1] + 3)

    index = 0
    children = []

    while (index < len(data)):
        if ((index + 3) < len(data)) and (data[index + 3] - data[index] == 3):
            children.append(3)
        elif ((index + 2) < len(data)) and (data[index + 2] - data[index] <= 3):
            children.append(2)
        else:
            children.append(1)
        index += 1

    arrangements = 1
    multiplier = 0

    for i in range(0, len(children)):
        if (multiplier >= 2) and (children[i] == 1):
            if (multiplier > 2): multiplier -= 1
            arrangements *= multiplier
            multiplier = 0
        elif (children[i] > 1):
            multiplier += children[i]

    print(arrangements)


if __name__ == '__main__':
    main()
