import sys

def check_current_number(number, preamble):
    found = False

    for i in range(0,len(preamble)-1):
        for j in range(1,len(preamble)):
            if preamble[i] + preamble[j] == number:
                found = True
                break

    return found


def get_invalid_number(data, preamble_size):
    number_ok = True
    preamble_index = 0

    while number_ok:
        current_number = data[preamble_index + preamble_size]
        number_ok = check_current_number(current_number, data[preamble_index:preamble_index + preamble_size])
        preamble_index += 1

    return current_number

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    data = [int(line) for line in lines]
    preamble_size = 25
    invalid_number = get_invalid_number(data, preamble_size)
    print("Invalid number: %d " % invalid_number)

if __name__ == '__main__':
    main()
