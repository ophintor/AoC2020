import timeit
from copy import deepcopy


def calculate_score(deck):
    total = 0

    for i in range(len(deck)):
        total += deck[i] * (len(deck) - i)

    return total


def recursive_combat(d1, d2, game):
    round = 0
    played_hashes_list = []

    while len(d1) > 0 and len(d2) > 0:
        round += 1

        # Using frozenset means that the order does no matter and therefore
        # it runs way faster. It works for the current input but might not
        # work for others!
        played_hash = tuple([frozenset(d1), frozenset(d2)])
        # played_hash = tuple([tuple(d1), tuple(d2)])

        if played_hash in played_hashes_list:
            score = calculate_score(d1)
            return 1
        else:
            played_hashes_list.append(played_hash)
            card1, card2 = d1[0], d2[0]
            del d1[0], d2[0]

            if card1 <= len(d1) and card2 <= len(d2):
                rd1, rd2 = deepcopy(d1[0:card1]), deepcopy(d2[0:card2])
                winner = recursive_combat(rd1, rd2, game + 1)
                d1.extend((card1, card2)) if winner == 1 else d2.extend((card2, card1))
            else:
                d1.extend((card1, card2)) if card1 > card2 else d2.extend((card2, card1))

    return 2 if len(d1) == 0 else 1


def main():
    start = timeit.default_timer()
    with open('input.txt') as f: input = f.read()

    p1_deck = [ int(x) for x in input.split('\n\n')[0].strip().split('\n')[1:] ]
    p2_deck = [ int(x) for x in input.split('\n\n')[1].strip().split('\n')[1:] ]

    winner = recursive_combat(p1_deck, p2_deck, 1)
    winner_deck = p1_deck if winner == 1 else p2_deck
    print(calculate_score(winner_deck))

    stop = timeit.default_timer()
    print("Time : %.4f ms" % (1000 * (stop - start)))


if __name__ == '__main__':
    main()
