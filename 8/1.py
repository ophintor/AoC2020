import sys

def main():
    filename = 'input.txt'
    instructions = []

    with open(filename) as f:
        lines = f.readlines()

    for line in lines:
        instructions.append([0,line[:-1]])

    index = 0
    acc = 0

    while (instructions[index][0] == 0):
        instructions[index][0] = 1
        operation = instructions[index][1].split(' ')[0]
        argument = int(instructions[index][1].split(' ')[1])

        if operation == "nop":
            index += 1
        elif operation == "acc":
            acc += argument
            index += 1
        elif operation == "jmp":
            index += argument


    print(acc)

if __name__ == '__main__':
    main()
