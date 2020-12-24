import timeit
import os

def main():
    start = timeit.default_timer()
    cwd = os.path.dirname(os.path.realpath(__file__)
    with open(cwd + '/example.txt') as f: lines = f.readlines()

    # Code here

    stop = timeit.default_timer()
    print("Time : %.4f ms" % (1000 * (stop - start)))


if __name__ == '__main__':
    main()
