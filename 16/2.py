import timeit
import re


def find_valid_values(lines):
    valid_values = {}

    for line in lines:
        if re.search('[a-z]*[: ]{1}[0-9]', line.strip()):
            field = line.split(":")[0]
            valid_values[field] = []

            range1 = line.split(":")[1].split('or')[0].strip()
            for i in range(int(range1.split('-')[0]), int(range1.split('-')[1]) + 1):
                valid_values[field].append(i)

            range2 = line.split(":")[1].split('or')[1].strip()
            for i in range(int(range2.split('-')[0]), int(range2.split('-')[1]) + 1):
                valid_values[field].append(i)
        else:
            break

    return valid_values


def find_valid_tickets(lines, valid_values):
    valid_tickets = []

    for line in lines:
        if re.search('([0-9]*[,]+).*', line.strip()):
            for value in line.split(","):
                found = False
                for field in valid_values.keys():
                    if int(value) in valid_values[field]:
                        found = True
                if not found:
                    break
            if found:
                valid_tickets.append(line.strip())

    return valid_tickets


def find_my_ticket(lines):
    for i in range(0, len(lines)):
        if re.search("^your ticket", lines[i]):
            return lines[i + 1].strip().split(",")


def are_fields_unique(fields):
    unique = True

    for position in fields.keys():
        if len(fields[position]) > 1:
            unique = False
            break

    return unique


def find_fields_order(tickets, valid_values):
    fields = {}

    for position in range(0, len(valid_values)):
        fields[position] = []
        values = []

        for ticket in tickets:
            values.append(ticket.split(',')[position])

        for field in valid_values.keys():
            found = True
            for value in values:
                if int(value) not in valid_values[field]:
                    found = False
                    break
            if found:
                fields[position].append(field)

    while (not are_fields_unique(fields)):
        for position in fields.keys():
            if len(fields[position]) == 1:
                field_to_delete = fields[position][0]

                for position in fields.keys():
                    if len(fields[position]) > 1 and field_to_delete in fields[position]:
                        fields[position].remove(field_to_delete)

    return fields


def main():
    start = timeit.default_timer()

    solution = 1
    with open('input.txt') as f: lines = f.readlines()

    valid_values = find_valid_values(lines)
    valid_tickets = find_valid_tickets(lines, valid_values)
    fields = find_fields_order(valid_tickets, valid_values)
    departure_positions = [ x for x in fields if re.search("departure", fields[x][0]) ]
    my_own_ticket = find_my_ticket(lines)

    for pos in departure_positions:
        solution *= int(my_own_ticket[pos])

    print(solution)

    stop = timeit.default_timer()
    print("Time : %.4f ms" % (1000 * (stop - start)))


if __name__ == '__main__':
    main()
