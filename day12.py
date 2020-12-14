

if __name__ == '__main__':


    layout = []
    max_id = 0

    free_seat_list = list(range(884))
    with open("input11.txt", 'r') as input_file:

        line = input_file.readline()
        while(len(line) > 0):

            layout.append(list(line[:-1]))

            line = input_file.readline()

    print(simulate(layout))

