import sys

def find_number_of_bags(bags, key):
    amount = 0
    for item in bags[key]:
        if 'no other bags' in item:
            amount = 0
        else:
            key = ' '.join(item.split(' ')[1:-1])
            qty = int(item.split(' ')[0])
            amount += qty + (qty * find_number_of_bags(bags, key))

    return amount


def main():
    filename = 'input.txt'
    bags = {}

    with open(filename) as f:
        lines = f.readlines()

    for line in lines:
        key = line.split(" bags")[0]
        values = line.split('contain ')[1].split('.')[0].split(', ')
        bags[key] = values

    number_of_bags = find_number_of_bags(bags, "shiny gold")
    print(number_of_bags)

if __name__ == '__main__':
    main()
