def is_digit(c):
    ascii_code = ord(c)
    return ascii_code >= 48 and ascii_code <= 57

def validate_field(name, value):

    if name == 'byr':
        return len(value) ==4 and int(value) >= 1920 and int(value) <= 2002
    if name == 'iyr':
        return len(value) == 4 and int(value) >= 2010 and int(value) <= 2020
    if name == 'eyr':
        return len(value) == 4 and int(value) >= 2020 and int(value) <= 2030
    if name == 'hgt':
        ending = value[-2:]
        is_cm = ending == 'cm'
        is_in = ending == 'in'
        if not is_cm and not is_in:
            return False
        mag = int(value[:-2])
        if is_cm and mag >= 150 and mag <= 193:
            return True
        if is_in and mag >= 59 and mag <= 76:
            return True
        return False
    if name == 'hcl':
        if value[0] != '#' or len(value) != 7:
            return False
        for i in range(1,7):
            ascii_code = ord(value[i])
            if not(is_digit(value[i]) or (ascii_code >= 97 and ascii_code <= 102)):
                return False
        return True
    if name == 'ecl':
        possible_values = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        return value in possible_values
    if name == 'pid':
        return len(value) == 9 and all(is_digit(c) for c in value)
    return False

def validate_passport(passport_string):
    print(passport_string)
    required_fields = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid']
    #   'cid']

    entries = passport_string.split(' ')

    for entry in entries:
        print(entry)
        entry_name, entry_value = entry.split(':')
        if entry_name in required_fields:
            is_valid = validate_field(entry_name, entry_value)
            if is_valid:
                required_fields.remove(entry_name)
            else:
                print('invalid field ' + entry_name + ' : ' + entry_value)

    return len(required_fields) == 0

if __name__ == '__main__':

    num_valid_passports = 0

    with open("input04.txt", 'r') as input_file:

        passport_string = input_file.readline()
        while(len(passport_string) > 0):

            next_line = input_file.readline()
            if len(next_line) > 1:
                passport_string = passport_string[:-1] + ' ' + next_line
            else:
                passport_string = passport_string[:-1]
                if validate_passport(passport_string):
                    num_valid_passports = num_valid_passports + 1
                passport_string = input_file.readline()

    print(num_valid_passports)


