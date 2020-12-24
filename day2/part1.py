import sys

def verify(min_length, max_length, letter, password):
    if (min_length <= password.count(letter) <= max_length):
        return True
    else:
        return False

def main():
    total = 0
    # filename = 'example.txt'
    filename = 'input.txt'

    with open(filename) as f:
        lines = f.readlines()

    for line in lines:
        min_length = int(line.split("-")[0])
        max_length = int(line.split(" ")[0].split("-")[1])
        letter = line.split(" ")[1][:-1]
        password = line.split(":")[1][:-1]
        # print(min_length, max_length, letter, password)
        if verify(min_length, max_length, letter, password):
            total += 1

    print(total)

if __name__ == '__main__':
    main()
