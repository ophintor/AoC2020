import sys

def main():
    filename = 'input.txt'

    with open(filename) as f:
        lines = f.readlines()

    for value1 in lines:
        for value2 in lines:
            if (int(value1) + int(value2) == 2020):
                print (int(value1) * int(value2))
                sys.exit(0)

if __name__ == '__main__':
    main()
