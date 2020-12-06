import sys
import re

def are_entries_ok(entries):
    return ("byr" in entries and
            "iyr" in entries and
            "eyr" in entries and
            "hgt" in entries and
            "hcl" in entries and
            "ecl" in entries and
            "pid" in entries)

def is_year_ok(min, max, value):
    return (min <= value <= max)

def is_height_ok(value):
    return ((len(value) >=4) and
            (((value[-2:] == "cm") and (150 <= int(value[:-2]) <= 193)) or
             ((value[-2:] == "in") and ( 59 <= int(value[:-2]) <=  76))))

def is_hair_color_ok(value):
    return re.match('#[0-9a-f]{6}', value)

def is_eye_color_ok(value):
    return (value == "amb" or
            value == "blu" or
            value == "brn" or
            value == "gry" or
            value == "grn" or
            value == "hzl" or
            value == "oth")

def is_passport_id_ok(value):
    return re.match('^[0-9]{9}$', value)

def is_validation_ok(passport):
    validation_ok = True
    for entry in passport:
        key   = entry.split(":")[0]
        value = entry.split(":")[1]

        if (key == "byr") and (not is_year_ok(1920, 2002, int(value))):
            validation_ok = False
        elif (key == "iyr") and (not is_year_ok(2010, 2020, int(value))):
            validation_ok = False
        elif (key == "eyr") and (not is_year_ok(2020, 2030, int(value))):
            validation_ok = False
        elif (key == "hgt") and (not is_height_ok(value)):
            validation_ok = False
        elif (key == "hcl") and (not is_hair_color_ok(value)):
            validation_ok = False
        elif (key == "ecl") and (not is_eye_color_ok(value)):
            validation_ok = False
        elif (key == "pid") and (not is_passport_id_ok(value)):
            validation_ok = False

    return validation_ok


def process_passport(passport):
    print("Checking passport...")
    passport = passport[:-1].replace('\n', ' ').split(' ')

    entries = set()
    for entry in passport:
        entries.add(entry.split(':')[0])

    print(passport)
    return (are_entries_ok(entries) and is_validation_ok(passport))


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
