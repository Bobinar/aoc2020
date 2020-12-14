

def run_program_until_line_repeats(program):

    lines_run = []

    acc = 0

    pc = 0

    while(pc not in lines_run and pc < len(program)):

        lines_run.append(pc)
        instruction, argument = program[pc]


        if instruction == 'nop':
            pc = pc + 1
        elif instruction == 'acc':
            acc = acc + argument
            pc = pc + 1
        elif instruction == 'jmp':
            pc = pc + argument
        else:
            raise ValueError("invalid instruction " + instruction)
        #print(f'ran {instruction} ({argument}) => pc = {pc}, acc = {acc}')

    if pc == len(program):
        return acc
    else:
        return None





if __name__ == '__main__':
    total = 0

    with open("input08.txt", 'r') as input_file:

        line = input_file.readline()
        program = []

        while (len(line) > 0):

            instruction, argument_string = line[:-1].split(' ')

            argument_value = int(argument_string[1:])

            if argument_string[0] == '-':
                argument_value = - argument_value

            program.append((instruction, argument_value))

            line = input_file.readline()


    jmp_indices = []
    nop_indices = []

    for i in range(len(program)):
        instruction, argument = program[i]
        if instruction == 'jmp':
            jmp_indices.append(i)
        if instruction == 'nop':
            nop_indices.append(i)


    for jmp_index in jmp_indices:
        modified_program = program.copy()
        instruction, argument = modified_program[jmp_index]
        modified_program[jmp_index] = ('nop',argument)

        result = run_program_until_line_repeats(modified_program)
        if result is not None:
            print(result)
            break

    for nop_index in nop_indices:
        modified_program = program.copy()
        instruction, argument = modified_program[nop_index]
        modified_program[nop_index] = ('jmp', argument)

        result = run_program_until_line_repeats(modified_program)
        if result is not None:
            print(result)
            break

    #print(run_program_until_line_repeats(program))