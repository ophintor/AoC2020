import sys

def find_shiny_gold(bags, key):
    found = 0
    for item in bags[key]:
        if (found) or ('no other bags' in item):
            break
        elif ('shiny gold' in item):
            found = 1
        else:
            key = ' '.join(item.split(' ')[1:-1])
            found += find_shiny_gold(bags, key)

    return found


def main():
    filename = 'input.txt'
    bags = {}

    with open(filename) as f:
        lines = f.readlines()

    for line in lines:
        key = line.split(" bags")[0]
        values = line.split('contain ')[1].split('.')[0].split(', ')
        bags[key] = values

    shiny_gold = 0
    for key in bags:
        shiny_gold += find_shiny_gold(bags, key)

    print(shiny_gold)

if __name__ == '__main__':
    main()
