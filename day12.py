
def part1():

    current_x = 0
    current_y = 0
    current_orientation = 0

    with open("input12.txt", 'r') as input_file:

        line = input_file.readline()
        while(len(line) > 0):

            command = line[:-1]

            magnitude = int(command[1:])
            command = command[0]
            if command == 'F':
                if current_orientation == 0:
                    command = 'E'
                elif current_orientation == 90:
                    command = 'N'
                elif current_orientation == 180:
                    command = 'W'
                elif current_orientation == 270:
                    command = 'S'


            if command == 'N':
                current_y = current_y + magnitude
            elif command == 'S':
                current_y = current_y - magnitude
            elif command == 'E':
                current_x = current_x + magnitude
            elif command == 'W':
                current_x = current_x - magnitude

            if command == 'R':
                current_orientation = current_orientation - magnitude
            if command == 'L':
                current_orientation = current_orientation + magnitude

            while current_orientation < 0:
                current_orientation = 360 + current_orientation

            while current_orientation >= 360:
                current_orientation = current_orientation - 360



            line = input_file.readline()



    print(abs(current_x) + abs(current_y))

if __name__ == '__main__':

    current_x = 0
    current_y = 0
    waypoint_relative_x = 10
    waypoint_relative_y = 1

    with open("input12.txt", 'r') as input_file:

        line = input_file.readline()
        while(len(line) > 0):

            command = line[:-1]

            magnitude = int(command[1:])
            command = command[0]
            if command == 'F':
                current_x = current_x + waypoint_relative_x * magnitude
                current_y = current_y + waypoint_relative_y * magnitude


            if command == 'N':
                waypoint_relative_y = waypoint_relative_y + magnitude
            elif command == 'S':
                waypoint_relative_y = waypoint_relative_y - magnitude
            elif command == 'E':
                waypoint_relative_x = waypoint_relative_x + magnitude
            elif command == 'W':
                waypoint_relative_x = waypoint_relative_x - magnitude

            if command == 'R' or command == 'L':
                real_rotation = 0
                if command == 'R':
                    real_rotation = 360 - magnitude
                if command == 'L':
                    real_rotation = magnitude

                while real_rotation < 0:
                    real_rotation = 360 + real_rotation

                while real_rotation >= 360:
                    real_rotation = real_rotation - 360

                if real_rotation == 90:
                    next_w_x = - waypoint_relative_y
                    next_w_y = waypoint_relative_x
                elif real_rotation == 180:
                    next_w_x = - waypoint_relative_x
                    next_w_y = - waypoint_relative_y
                elif real_rotation == 270:
                    next_w_x = waypoint_relative_y
                    next_w_y = - waypoint_relative_x
                else:
                    next_w_x = waypoint_relative_x
                    next_w_y = waypoint_relative_y

                waypoint_relative_x = next_w_x
                waypoint_relative_y = next_w_y

            line = input_file.readline()



    print(abs(current_x) + abs(current_y))

