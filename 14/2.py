import sys
import re

def apply_bitmask_on_address(address, mask):
    binary_list = list("{0:b}".format(address).zfill(len(mask)))
    for i in range(0, len(mask)):
        if mask[i] != '0': binary_list[i] = mask[i]

    return ''.join(binary_list)


def get_list_of_addresses(address_mask):
    list_of_addresses = []
    address_mask_list = list(address_mask)

    x_indexes = [ i for i in range(0,len(address_mask_list)) if address_mask_list[i] == 'X']
    x_combinations = 2 ** len(x_indexes)

    for i in range(0, x_combinations):
        bits = list("{0:b}".format(i).zfill(len(x_indexes)))
        bit_index = 0
        new_address = [x for x in address_mask]
        for x_index in x_indexes:
            new_address[x_index] = str(bits[bit_index])
            bit_index += 1
        list_of_addresses.append(int(''.join(new_address),2))

    return list_of_addresses


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
            address_mask = apply_bitmask_on_address(address, mask)
            list_of_addresses = get_list_of_addresses(address_mask)
            for masked_address in list_of_addresses:
                memory[masked_address] = value


    print(sum(memory.values()))


if __name__ == '__main__':
    main()
