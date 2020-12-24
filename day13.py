import math

def lcm_pair(a, b):
    res = (a * b) / math.gcd ( a , b )
    return int(res)

def lcm_list(number_list):
    if len(number_list) > 2:
        return lcm_pair(number_list[0],lcm_list(number_list[1:]))
    if len(number_list) == 2:
        return lcm_pair(number_list[0], number_list[1])
    return number_list[0]

def gcd_list(number_list):
    if len(number_list) > 2:
        return math.gcd(number_list[0],gcd_list(number_list[1:]))
    if len(number_list) == 2:
        return math.gcd(number_list[0], number_list[1])
    return number_list[0]


def chinese_remainder(ais, mis):
    M = 1
    for i in range(len(mis)):
        M = M * mis[i]

    Mis = []
    Yis = []

    for i in range(len(mis)):
        Mi = int(M / mis[i])
        Mis.append(Mi)
        multiplier = 1
        while (Mi * multiplier) % mis[i] != 1:
            multiplier = multiplier + 1

        Yis.append(multiplier)

    t = 0
    for i in range(len(Mis)):
        t = t + (ais[i] * Mis[i] * Yis[i])

    print(t)
    print(M)
    print(t % M)



if __name__ == '__main__':

    with open("input13.txt", 'r') as input_file:

        line = input_file.readline()
        arrival_time = int(line)

        line = input_file.readline()
        bus_id_strings = line[:-1].split(',')
        bus_ids = []
        initial_departures = []
        i = 0
        for bus_id_string in bus_id_strings:
            if bus_id_string != 'x':
                bus_ids.append(int(bus_id_string))
                initial_departures.append(int(bus_id_string) - i)
            i = i + 1
        print(arrival_time)
        print(bus_ids)

        print(lcm_list(bus_ids))
        print(gcd_list(bus_ids))

        t = 0
        found = False

        max_id = -1
        max_id_position = -1
        for i in range(len(bus_ids)):
            if bus_ids[i] > max_id:
                max_id_position = i
                max_id = bus_ids[i]

        t = max_id - initial_departures[max_id_position]


        chinese_remainder(initial_departures,bus_ids)
        #chinese remainder theorem

        #chinese_remainder([6,4],[7,8])
        #chinese_remainder([1,2,3,4], [2,3,5,7])

        '''
        multiplier = 1

        t = 0
        for i in range(len(bus_ids)):

            m = bus_ids[i]
            a = initial_departures[i]

            while t % m != a:
                t = t + multiplier
            multiplier = multiplier * m

        #print(t)
        '''


        '''
        while not found:

            all_here = True

            for i in range(len(bus_ids)):
                bus_id = bus_ids[i]
                initial_departure = initial_departures[i]
                if (t + initial_departure) % bus_id != 0:
                    all_here = False
                    break

            if all_here:
                print(t)
                break

            t = t + max_id

        '''


        #1748774091859561 too high
        '''part1
        min_wait = 100000000000000000000
        min_id = -1
        for bus_id in bus_ids:
            wait_time = bus_id - (arrival_time % bus_id)
            if wait_time < min_wait:
                min_wait = wait_time
                min_id = bus_id

        print(min_wait * min_id)

        #266 too low
        '''