
if __name__ == '__main__':
    input_numbers = []
    total = 0
    with open("input01.txt", 'r') as input_file:
        new_line = input_file.readline()
        while(len(new_line) > 0):
            input_numbers.append(int(new_line))
            new_line = input_file.readline()


    for i in range(len(input_numbers)):
        for j in range(i+1, len(input_numbers)):
            for k in range(j + 1, len(input_numbers)):
                if input_numbers[i] + input_numbers[j] + input_numbers[k] == 2020:
                    print(input_numbers[i]*input_numbers[j]*input_numbers[k])

    print(input_numbers)