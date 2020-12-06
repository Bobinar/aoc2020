

def code_to_number(code):

    seat_number = 0
    n = 10#len(code)
    for i in range(n):

        if code[i] == 'B' or code[i] == 'R':
            seat_number = seat_number + pow(2, n-(i + 1))

    return seat_number

if __name__ == '__main__':

    print(code_to_number('BFFFBBFRRR'))

    max_id = 0

    free_seat_list = list(range(884))
    with open("input05.txt", 'r') as input_file:

        line = input_file.readline()
        while(len(line) > 0):

            id = code_to_number(line)
            free_seat_list.remove(id)
            max_id = max(max_id, id)

            line = input_file.readline()

        print(free_seat_list)

