import sys

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    data = [int(line) for line in lines]
    data.append(0)
    data.sort()
    data.append(data[len(data) - 1] + 3)

    ones = 0
    threes = 0

    for i in range(0,len(data)-1):
        if (data[i]+1 == data[i+1]):
            ones += 1
        elif (data[i]+3 == data[i+1]):
            threes += 1

    print(ones,threes,(ones * threes))


if __name__ == '__main__':
    main()
