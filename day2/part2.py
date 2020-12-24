import sys

def verify(pos1, pos2, letter, password):
    if (password[pos1-1] == letter or password[pos2-1] == letter) and (password[pos1-1] != password[pos2-1]):
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
        pos1 = int(line.split("-")[0])
        pos2 = int(line.split(" ")[0].split("-")[1])
        letter = line.split(" ")[1][:-1]
        password = line.split(" ")[2][:-1]
        # print(pos1, pos2, letter, password)
        if verify(pos1, pos2, letter, password):
            total += 1

    print(total)

if __name__ == '__main__':
    main()
