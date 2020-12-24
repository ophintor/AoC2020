import timeit
import re


def format_rules(rules, key, depth):
    # Increasing the max_depth gives the same solution for *this* input but might not be enough for a different one
    max_depth = 4
    rules_set = set(re.findall('[0-9]+', rules[key]))
    suffix = ""

    if rules_set:
        if str(key) in rules_set:
            depth += 1

        for rule in rules_set:
            if depth < max_depth:
                rules[key] = re.sub(r'\b%s\b' % rule, '(' + format_rules(rules, int(rule), depth) + ')', rules[key])

    return rules[key]


def get_rules_and_messages(lines):
    rules = {}
    message = []

    for line in lines:
        if re.search(':',line):
            index = int(line.split(':')[0].strip())
            rules[index] = line.split(':')[1].strip()
            if '\"' in rules[index]:
                rules[index] = rules[index][1:-1]
        elif line != '\n':
            message.append(line.strip())

    regex = "^" + format_rules(rules, 0, 0).replace(' ','').replace('(a)','a').replace('(b)','b') + "$"

    return regex, message


def check_valid_messages(regex, messages):
    total = 0

    for m in messages:
        if re.search(regex, m):
            total += 1

    return total


def main():
    start = timeit.default_timer()
    with open('input2.txt') as f: lines = f.readlines()

    regex, messages = get_rules_and_messages(lines)
    print(check_valid_messages(regex, messages))

    stop = timeit.default_timer()
    print("Time : %.4f ms" % (1000 * (stop - start)))


if __name__ == '__main__':
    main()
