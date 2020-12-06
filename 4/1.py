import sys

def are_entries_ok(entries):
    return ("byr" in entries and
            "iyr" in entries and
            "eyr" in entries and
            "hgt" in entries and
            "hcl" in entries and
            "ecl" in entries and
            "pid" in entries)

def process_passport(passport):
    print("Checking passport...")
    passport = passport[:-1].replace('\n', ' ').split(' ')

    entries = set()
    for entry in passport:
        entries.add(entry.split(':')[0])

    print(passport)
    return (are_entries_ok(entries))


def main():
    filename = 'input.txt'
    valid_passports = 0
    passport = ""

    with open(filename) as f:
        lines = f.readlines()

    for line in lines:
        if line != '\n':
            passport += line
        else:
            valid_passport = process_passport(passport)
            valid_passports += valid_passport
            print("Valid passports: %d" % valid_passports)
            passport = ""

    valid_passport = process_passport(passport)
    valid_passports += valid_passport
    print("Valid passports: %d" % valid_passports)


if __name__ == '__main__':
    main()
