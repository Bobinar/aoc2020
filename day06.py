
def add_unique_letters(line, current_group_letters):
    for c in line:
        if c == '\n':
            continue
        if c not in current_group_letters:
            current_group_letters.append(c)


def part1():
    total = 0

    with open("input06.txt", 'r') as input_file:

        line = input_file.readline()

        current_group_letters = []
        while(len(line) > 0):

            add_unique_letters(line,current_group_letters)
            next_line = input_file.readline()

            while len(next_line) > 1:
                add_unique_letters(next_line,current_group_letters)
                next_line = input_file.readline()

            total = total + len(current_group_letters)
            current_group_letters = []
            line = input_file.readline()

    print(total)


def delete_non_overlapping_letters(line, current_group_letters):
    i = 0
    while i < len(current_group_letters):
        c = current_group_letters[i]
        if c not in line:
            current_group_letters.remove(c)
        else:
            i = i + 1



if __name__ == '__main__':
    total = 0

    with open("input06.txt", 'r') as input_file:

        line = input_file.readline()


        while (len(line) > 0):
            current_group_letters = list(line[:-1])

            next_line = input_file.readline()

            while len(next_line) > 1:
                delete_non_overlapping_letters(next_line, current_group_letters)
                next_line = input_file.readline()

            total = total + len(current_group_letters)

            line = input_file.readline()

    print(total)