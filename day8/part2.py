import sys

def init_instructions(lines):
    instructions = []
    for line in lines:
        instructions.append([0,line[:-1]])

    return instructions

def main():
    filename = 'input.txt'
    instructions = []

    with open(filename) as f:
        lines = f.readlines()

    for i in range(0,len(lines)):
        instructions = init_instructions(lines)
        index = 0
        acc = 0

        if "jmp" in instructions[i][1]:
            instructions[i][1] = instructions[i][1].replace("jmp", "nop")
        elif "nop" in instructions[i][1]:
            instructions[i][1] = instructions[i][1].replace("nop", "jmp")

        while instructions[index][0] == 0:
            completed = 0
            instructions[index][0] = 1
            operation = instructions[index][1].split(' ')[0]
            argument = int(instructions[index][1].split(' ')[1])

            if operation == "nop":
                if (index + 1) == len(instructions):
                    completed = 1
                else:
                    index += 1
            elif operation == "acc":
                acc += argument
                if (index + 1) == len(instructions):
                    completed = 1
                else:
                    index += 1
            elif operation == "jmp":
                if (index + argument) == len(instructions):
                    completed = 1
                else:
                    index += argument

            if completed:
                print("Completed!")
                print(acc)
                sys.exit(0)



if __name__ == '__main__':
    main()
