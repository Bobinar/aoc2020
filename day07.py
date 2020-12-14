
#part2
def number_of_bags_contained_in_color(color, contains_graph):
    contained = contains_graph[color]
    count = 0
    i = 0
    while i < len(contained):
        current_number, current_color = contained[i]
        count = count + current_number
        contained_by_current = contains_graph[current_color]
        for inside_number, inside_color in contained_by_current:
            contained.append((current_number * inside_number, inside_color))
        i = i + 1

    return count

#part1
def colors_that_can_contain(color, is_contained_by_graph):
    contained_by = is_contained_by_graph[color].copy()

    i = 0
    while i < len(contained_by):
        current_color = contained_by[i]

        if current_color in is_contained_by_graph.keys():
            colors_that_contain_current = is_contained_by_graph[current_color]

            for candidate_color in colors_that_contain_current:
                if candidate_color not in contained_by:
                    contained_by.append(candidate_color)

        i = i + 1



    return contained_by




if __name__ == '__main__':
    total = 0

    with open("input07.txt", 'r') as input_file:

        line = input_file.readline()

        contains_graph = dict()
        is_contained_by_graph = dict()

        while (len(line) > 0):

            container, contents = line.split(' contain ')

            container = container.split(' ')[0:2]
            container = container[0]+container[1]


            contents = contents[:-2]

            products = contents.split(', ')

            contains_graph[container] = []

            for product in products:
                if product == 'no other bags':
                    continue
                product_pieces = product.split(' ')
                number = int(product_pieces[0])
                product_color = product_pieces[1] + product_pieces[2]
                contains_graph[container].append((number, product_color))

                if product_color not in is_contained_by_graph.keys():
                    is_contained_by_graph[product_color] = []
                is_contained_by_graph[product_color].append(container)


            #print(products)
            #print(container)


            line = input_file.readline()

    print(len(colors_that_can_contain('shinygold', is_contained_by_graph)))

    print(number_of_bags_contained_in_color('shinygold', contains_graph))