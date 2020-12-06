import sys

def main():
    filename = 'input.txt'
    total = 0
    group = ""

    with open(filename) as f:
        lines = f.readlines()

    lines.append('\n')

    for line in lines:
        if (line != '\n'):
            group += line
        else:
            group_list = group[:-1].split('\n')
            # print("\n")
            # print("* group list *")
            # print(group_list)
            answers_set = set(group_list[0])
            for person in group_list:
                # print("intersecting %s and %s" % (person, str(answers_set)))
                answers_set = answers_set.intersection(set(person))
                # print(str(answers_set))
            answers = len(answers_set)
            # print ("Answers: %d " % answers)

            total += answers
            group = ""

    print(total)


if __name__ == '__main__':
    main()
