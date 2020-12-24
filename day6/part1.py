import sys

def main():
    filename = 'input.txt'
    total = 0
    group = ""

    with open(filename) as f:
        lines = f.readlines()

    lines.append('\n')

    for line in lines:
        if line != '\n':
            group += line.replace('\n','')
        else:
            # print(group)
            answers = len(set(group))
            total += answers
            group = ""

    print(total)


if __name__ == '__main__':
    main()
