import copy

directions = []

for i in range(-1, 2):
    for j in range(-1, 2):
        if i == 0 and j == 0:
            continue
        directions.append((i, j))


def occupied_diretion(direction, x, y, layout):
    i = x + direction[0]
    j = y + direction[1]

    while(i >= 0 and i <len(layout) and j >= 0 and j < len(layout[0])):
        if layout[i][j] == '#':
            return 1
        if layout[i][j] == 'L':
            return 0
        i = i + direction[0]
        j = j + direction[1]

    return 0

def occupied_directions(x, y, layout):
    count = 0

    for direction in directions:
        count = count + occupied_diretion(direction, x, y, layout)

    return count



def occupied_8_neighbours(x, y, layout):
    count = 0

    for i in range(max(x-1,0),min(x+2,len(layout))):
        for j in range(max(y - 1, 0), min(y + 2, len(layout[0]))):
            if i == x and j == y:
                continue
            if layout[i][j] == '#':
                count = count + 1

    return count


def simulate(layout):

    previous = layout
    iterations = 0
    something_changed = True
    while(something_changed):
        layout = copy.deepcopy(previous)
        iterations = iterations + 1
        something_changed = False
        for i in range(len(layout)):
            for j in range(len(layout[0])):
                if previous[i][j] == 'L' and occupied_directions(i,j,previous) == 0:
                    layout[i][j] = '#'
                    something_changed = True
                elif previous[i][j] == '#' and occupied_directions(i,j,previous) >= 5: # 4 in first part
                    layout[i][j] = 'L'
                    something_changed = True
        previous = layout

        print(iterations)
    occupied_seats = sum(map(lambda x: sum(map(lambda y: y == '#', x)), layout))
    return occupied_seats


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

