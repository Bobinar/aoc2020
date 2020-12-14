

def are_there(i, numbers):
    value = numbers[i]
    for j in range(i - 25, i):
        for k in range(j + 1, i):
            if numbers[j] + numbers[k] == value:
                return True

    return False




def part1(numbers):
    PREAMBLE = 25

    for i in range(25,len(numbers)):

        if not are_there(i,numbers):
            print(numbers[i])
            break




if __name__ == '__main__':


    numbers = []
    max_id = 0

    with open("input09.txt", 'r') as input_file:

        line = input_file.readline()
        while(len(line) > 0):

            numbers.append(int(line[:-1]))

            line = input_file.readline()

    print(numbers)

    cool_value = 22477624

    range_sum = 0
    range_start = 0
    range_end = 0

    for i in range(len(numbers)):
        if range_sum == cool_value:
            print(min(numbers[range_start:range_end+1]) + max(numbers[range_start:range_end + 1]))
            break
        if range_sum < cool_value:
            range_end = range_end + 1
            range_sum = range_sum + numbers[i]
            while range_sum > cool_value:
                range_sum = range_sum - numbers[range_start]
                range_start = range_start + 1





