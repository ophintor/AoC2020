import sys
import re

def update_memory_address(memory, address, mask):
    binary_list = list("{0:b}".format(memory[address]).zfill(len(mask)))
    for i in range(0, len(mask)):
        if mask[i] != 'X': binary_list[i] = mask[i]

    return int(''.join(binary_list), 2)


def main():
    with open('input.txt') as f:
        lines = f.readlines()

    memory = {}

    for line in lines:
        if re.search("^mask", line):
            mask = line.split('=')[1].strip()
        else:
            address = int(line.split('[')[1].split(']')[0])
            value = int(line.split('=')[1].strip())
            memory[address] = value
            memory[address] = update_memory_address(memory, address, mask)

    print(sum(memory.values()))


if __name__ == '__main__':
    main()
