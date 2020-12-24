import timeit
import re


def calculate_expression(exp):
    result = exp.split()

    while '+' in result:
        result[result.index("+") - 1] = str(eval(''.join(result[result.index("+") - 1:result.index("+") + 2])))
        del result[result.index("+"):result.index("+") + 2]

    return int(eval(''.join(result)))


def calculate_line(exp):
    regex = '\([0-9\+\*\ ]*\)'
    while re.search(regex, exp):
        exp = re.sub(regex, str(calculate_expression(re.search(regex, exp)[0][1:-1])), exp, count = 1)

    return calculate_expression(exp)


def main():
    start = timeit.default_timer()
    with open('input.txt') as f: lines = f.readlines()

    result = 0
    for exp in lines:
        result += calculate_line(exp.strip())

    print(result)

    stop = timeit.default_timer()
    print("Time : %.4f ms" % (1000 * (stop - start)))


if __name__ == '__main__':
    main()
