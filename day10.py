# too low 6200896666048

memo = dict()

def recursive_thing(current_index, adapters):
    if current_index >= len(adapters) -1:
        return 1
    if current_index in memo.keys():
        return memo[current_index]

    current_joltage = adapters[current_index]
    options = 0
    for i in range(1, min(4, len(adapters) - current_index)):
        if adapters[i + current_index] <= current_joltage + 3:
            options = options + recursive_thing(i + current_index, adapters)
    memo[current_index] = options
    return options




if __name__ == '__main__':


    adapters = [0]


    with open("input10.txt", 'r') as input_file:

        line = input_file.readline()
        while(len(line) > 0):

            adapters.append(int(line[:-1]))

            line = input_file.readline()


    current_joltage = 0

    adapters = sorted(adapters)
    adapters.append(adapters[-1] + 3)
    diff_1 = 0
    diff_3 = 0

    i = 0
    while i < len(adapters):
        next_joltage = adapters[i]
        difference = next_joltage - current_joltage

        if difference == 1:
            diff_1 = diff_1 + 1
        if difference == 3:
            diff_3 = diff_3 + 1

        current_joltage = next_joltage
        i = i + 1




    print(diff_1 * diff_3)


    print(recursive_thing(0,adapters))