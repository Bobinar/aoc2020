

def int_to_binary_string(value):
    return "{0:b}".format(value)

def binary_string_to_value(string):
    return int(string, 2)


def modify_value_with_mask(value,mask):
    result = ''
    length = len(mask)

    for i in range(length):
        index = length - i - 1
        if mask[index] == 'X':
            value_index = len(value) - i - 1
            if value_index >= 0:
                result = value[value_index] + result
            else:
                result = '0' + result
        else:
            result = mask[index] + result
    return result

def part1():

    current_mask = None

    MEM_SIZE = 2**36
    memory = dict()

    with open("input14.txt", 'r') as input_file:
        line = input_file.readline()
        while(len(line) > 0):
            line_split = line[:-1].split(' = ')

            destination = line_split[0]
            parameter = line_split[1]

            if destination == 'mask':
                current_mask = parameter
                print(current_mask)
            else:
                address = int(destination[4:-1])
                print(address)


                binary_string = int_to_binary_string(int(parameter))
                print(f'{parameter} = {binary_string}')

                result = modify_value_with_mask(binary_string,current_mask)
                print(current_mask)
                print(result)

                memory[address] = binary_string_to_value(result)

            line = input_file.readline()

    accum = 0
    for key in memory.keys():
        accum = accum + memory[key]
        print(f'adding {memory[key]} from address {key}')

    print(accum)

    # 10845151042338 too high
    # 8570568288597

def modify_value_with_mask_p2(value,mask):
    result = ''
    length = len(mask)

    for i in range(length):
        index = length - i - 1
        if mask[index] == '0':
            value_index = len(value) - i - 1
            if value_index >= 0:
                result = value[value_index] + result
            else:
                result = '0' + result
        else:
            result = mask[index] + result
    return result

def get_all_addresses_covered(address_with_wildcards):

    current_addresses = ['']

    for i in range(len(address_with_wildcards)):
        c = address_with_wildcards[i]
        if c != 'X':
            for j in range(len(current_addresses)):
                current_addresses[j] = current_addresses[j] + c
        else:
            for j in range(len(current_addresses)):
                ori = current_addresses[j]
                current_addresses[j] = ori + '0'
                current_addresses.append(ori + '1')

    return current_addresses







if __name__ == '__main__':
    current_mask = None

    MEM_SIZE = 2**36
    memory = dict()

    with open("input14.txt", 'r') as input_file:
        line = input_file.readline()
        while(len(line) > 0):
            line_split = line[:-1].split(' = ')

            destination = line_split[0]
            parameter = line_split[1]

            if destination == 'mask':
                current_mask = parameter
                print(current_mask)
            else:
                address = int(destination[4:-1])
                print(address)


                binary_string = int_to_binary_string(address)
                print(f'{address} = {binary_string}')

                result = modify_value_with_mask_p2(binary_string, current_mask)
                print(current_mask)
                print(result)

                for address_covered in get_all_addresses_covered(result):
                    print(address_covered)
                    memory[binary_string_to_value(address_covered)] = int(parameter)

            line = input_file.readline()

    accum = 0
    for key in memory.keys():
        accum = accum + memory[key]
        print(f'adding {memory[key]} from address {key}')

    print(accum)

    # 10845151042338 too high
    # 8570568288597
