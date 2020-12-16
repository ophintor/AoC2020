import timeit


def main():
    start = timeit.default_timer()
    with open('example.txt') as f: lines = f.readlines()

    # Code here

    stop = timeit.default_timer()
    print("Time : %.4f ms" % (1000 * (stop - start)))


if __name__ == '__main__':
    main()
