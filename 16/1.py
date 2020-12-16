import timeit
import re


def main():
    start = timeit.default_timer()
    with open('input.txt') as f: lines = f.readlines()

    valid_values = set()
    found_values = []

    for line in lines:
        if re.search('[a-z]*[: ]{1}[0-9]', line.strip()):
            range1 = line.split(":")[1].split('or')[0].strip()
            range2 = line.split(":")[1].split('or')[1].strip()
            for i in range(int(range1.split('-')[0]), int(range1.split('-')[1]) + 1):
                valid_values.add(i)
            for i in range(int(range2.split('-')[0]), int(range2.split('-')[1]) + 1):
                valid_values.add(i)
        elif re.search('^your ticket', line.strip()):
            lines[lines.index(line) + 1] = ''
        elif re.search('([0-9]*[,]+).*', line.strip()):
            for i in line.split(','):
                found_values.append(int(i))

    total = 0
    for i in found_values:
        if i not in valid_values:
            total += i

    print(total)

    stop = timeit.default_timer()
    print("Time : %.4f ms" % (1000 * (stop - start)))


if __name__ == '__main__':
    main()
