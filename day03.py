

def trees_in_line(lines,dx,dy):
    horizontal_step = dx
    vertical_step = dy

    x = 0
    y = 0

    step_number = 0
    tree_count = 0
    while y < len(lines):

        if lines[y][x % len(lines[0])] == '#':
            tree_count = tree_count + 1

        step_number = step_number + 1
        x = x + horizontal_step
        y = y + vertical_step


    return tree_count

if __name__ == '__main__':

    total_bad = 0
    lines=[]
    with open("input03.txt", 'r') as input_file:
        new_line = input_file.readline()
        while(len(new_line) > 0):
            lines.append(new_line[:-1])
            new_line = input_file.readline()

    print(trees_in_line(lines,3,1) * trees_in_line(lines,1,1) * trees_in_line(lines,5,1) * trees_in_line(lines,7,1) *trees_in_line(lines,1,2))


