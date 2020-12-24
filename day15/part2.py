import timeit

def main():
    start = timeit.default_timer()

    with open('input.txt') as f:
        lines = f.readlines()

    nth_number = 30000000
    starting_numbers = lines[0].split(',')
    spoken_last = {}

    for i in range(0, len(starting_numbers)):
        spoken_last[int(starting_numbers[i])] = [i + 1, i + 1]
        last_number = int(starting_numbers[i])

    for i in range(len(starting_numbers), nth_number):
        if last_number in spoken_last.keys():
            spoken_last[last_number][0] = spoken_last[last_number][1]
            spoken_last[last_number][1] = i
        else:
            spoken_last[last_number] = [i, i]

        last_number = spoken_last[last_number][1] - spoken_last[last_number][0]

    print(last_number)
    stop = timeit.default_timer()
    print("Time : %.4f ms" % (1000 * (stop - start)))


if __name__ == '__main__':
    main()
