
if __name__ == '__main__':

    total_bad = 0
    with open("input02.txt", 'r') as input_file:
        new_line = input_file.readline()
        while(len(new_line) > 0):
            #input_numbers.append(int(new_line))

            new_line_split = new_line.split(':')
            policy_split = new_line_split[0].split(' ')

            policy_char = policy_split[1][0]

            numbers = policy_split[0].split('-')

            min_number = int(numbers[0])
            max_number = int(numbers[1])

            password = new_line_split[1]

            print(f'{min_number} {max_number} {policy_char} {password}')

            times_the_char_appears = password.count(policy_char)

            #part1===> if times_the_char_appears >= min_number and times_the_char_appears <= max_number:
            if (password[min_number] == policy_char) ^ (password[max_number] == policy_char):
                total_bad = total_bad + 1


            new_line = input_file.readline()



    print(total_bad)