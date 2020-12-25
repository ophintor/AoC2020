import timeit
import os

def calculate_loop_size(pub_key, remainder, subject_number = 7):
    n = subject_number
    loop_size = 1

    while n != pub_key:
        n = (n * subject_number) % remainder
        loop_size += 1

    return loop_size


def calculate_enc_key(pub_key, loop_size, remainder):
    key = pub_key

    for i in range(1, loop_size):
        key = (key * pub_key) % remainder

    return key


def main():
    start = timeit.default_timer()
    cwd = os.path.dirname(os.path.realpath(__file__))
    with open(cwd + "/input.txt") as f: lines = f.readlines()

    card_pub_key, door_pub_key = int(lines[0].strip()), int(lines[1].strip())
    remainder = 20201227

    card_loop_size = calculate_loop_size(card_pub_key, remainder)
    door_loop_size = calculate_loop_size(door_pub_key, remainder)
    enc_key = calculate_enc_key(door_pub_key, card_loop_size, remainder)
    print(enc_key)

    stop = timeit.default_timer()
    print("Time : %.4f ms" % (1000 * (stop - start)))


if __name__ == '__main__':
    main()
