import timeit


def is_dictionary_complete(dictionary):
    ready = True

    for i in dictionary.keys():
        if len(dictionary[i]) > 1:
            ready = False
            break

    return ready


def remove_unique_entries(dictionary):
    for i in dictionary.keys():
        for j in dictionary.keys():
            if len(dictionary[i]) == 1 and list(dictionary[i])[0] in dictionary[j] and i != j:
                dictionary[j].remove(list(dictionary[i])[0])


def generate_dictionary(whole_thing, all_allergens, all_ingredients):
    dictionary = {}

    for i in all_ingredients:
        dictionary[i] = set()

    for a in all_allergens:
        for i in all_ingredients:
            match = True
            for thing in whole_thing.keys():
                if a not in whole_thing[thing][0] and i in whole_thing[thing][1]:
                    match = False
            if match:
                dictionary[i].add(a)

    while not is_dictionary_complete(dictionary):
        remove_unique_entries(dictionary)

    return dictionary


def main():
    start = timeit.default_timer()
    with open('input.txt') as f: lines = f.readlines()

    all_allergens = set()
    all_ingredients = set()
    whole_thing = {}
    count = 0

    for food in lines:
        allergens = food.split('contains')[1].strip()[:-1].split(', ')
        ingredients = food.split('contains')[0][:-1].strip().split(' ')
        whole_thing[count] = [ingredients, allergens]
        count += 1

        for allergen in ingredients:
            all_allergens.add(allergen)

        for ingredient in allergens:
            all_ingredients.add(ingredient)

    d = generate_dictionary(whole_thing, all_allergens, all_ingredients)
    allergens_to_remove = [ list(x)[0] for x in d.values() ]

    solution = 0
    for k in whole_thing.keys():
        solution += len(set(whole_thing[k][0]) - set(allergens_to_remove))

    print(solution)

    stop = timeit.default_timer()
    print("Time : %.4f ms" % (1000 * (stop - start)))


if __name__ == '__main__':
    main()
