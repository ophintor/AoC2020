import timeit


def get_higher_card(d1, d2):
    if d1[0] > d2[0]:
        d1.append(d1[0])
        d1.append(d2[0])
    else:
        d2.append(d2[0])
        d2.append(d1[0])

    del d1[0]
    del d2[0]


def calculate_score(deck):
    total = 0
    for i in range(len(deck)):
        total += deck[i] * (len(deck) - i)

    return total


def main():
    start = timeit.default_timer()
    with open('input.txt') as f: input = f.read()

    p1_deck = [ int(x) for x in input.split('\n\n')[0].strip().split('\n')[1:] ]
    p2_deck = [ int(x) for x in input.split('\n\n')[1].strip().split('\n')[1:] ]

    while len(p1_deck) > 0 and len(p2_deck) > 0:
        get_higher_card(p1_deck, p2_deck)

    if len(p1_deck) > len(p2_deck):
        winner_deck = p1_deck
    else:
        winner_deck = p2_deck

    print(calculate_score(winner_deck))

    stop = timeit.default_timer()
    print("Time : %.4f ms" % (1000 * (stop - start)))


if __name__ == '__main__':
    main()
