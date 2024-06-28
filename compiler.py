# FIXME bad module name

mce = 'MASML compile error'
ctc = 'c-type (command-type)'
oop = 'out of program'
rtc = 'r-type (run-type)'

# TODO use type annotations
# FIXME global is SUCK
variables = dict()


# TODO use type annotations
# TODO select AKA StreamIO for console output

def console(com):
    if com[0] == '*o':
        if com[1] in variables.keys():
            print(variables[com[1]][0])

        else:
            if not com[1][0] == com[1][-1] == "\"":
                print(com[1][1:], end=' ')
                i = 2

                while com[i][-1] != "\"":
                    print(com[i], end=' ')
                    i += 1
                print(com[i][:-1])

            else:
                print(com[1][1:-1])

    # FIXME code duplication

    elif com[0] == '*i':
        if variables[com[1]][1] == '#b':
            variables[com[1]][0] = int(input())

        elif variables[com[1]][1] == '#i':
            variables[com[1]][0] = int(input())


# TODO select AKA StreamIO for error output
# TODO use type annotations
def variable(com):
    if com[1] in variables.keys():
        print(f"{mce}: recreating variable {com[1]}")
        exit(1)  # TODO use Exceptions

    elif com[0] == '#b':
        variables[com[1]] = [int(com[2]), '#b']

    elif com[0] == '#i':
        variables[com[1]] = [int(com[2]), '#i']


# TODO use Exceptions
def deInit(com):
    if com[0] not in variables.keys():
        print(f"{mce}:  uninitialized variable {com[1]}")
        exit(1)

    variables.pop(com[0])


def clear():
    global variables
    variables.clear()


# TODO use type annotations
def run(*programs):
    for program in programs:
        for string in program:
            match string[0]:
                case 'c':
                    console(string[1:])

                case 'v':
                    variable(string[1:])

                case 'd':
                    deInit(string[1:])

                case 'x':
                    clear()

                case _:  # TODO use Exceptions
                    print(f"{mce}: MASML error in code")
                    exit(1)


program_index = -1  # FIXME global is SUCK


# FIXME BRO TO MUCH TABS
def main(filename: str):
    with open(filename, 'r') as f:
        source_lines = f.read().split('.')  # Bad variable name fixed
        programs = list()

    # FIXME inner function without reason
    def maider(__file):  # name conflict fixed
        global program_index

        for i in range(len(__file)):
            token = __file[i]
            if '$' in token:
                token = token[:token.index('$')]
            token = token.split()
            if len(token) == 0:
                continue
                # TODO use Exceptions
            if token[0] in ('v', 'c', 'l', 'f', 'd', 'a', 'w', 'i', 'e', 'z'):  # tuple for memory save
                if program_index == -1:
                    print(f"{mce}: string {' '.join(token)} is a {ctc} string {oop}")
                    exit(1)
                else:
                    if len(programs) <= program_index:
                        programs.append([token[:token.index(';')]])
                    else:
                        programs[program_index].append(token[:token.index(';')])
            else:
                match token[0]:
                    case "m":
                        if token[1] == 'stdlib':
                            import stdlib
                            new_file = stdlib.import_stdlib(token[2], "\n".join(__file[i + 1:]))
                            maider(new_file.splitlines())
                    # TODO use Exceptions
                    case "p":
                        if token[2] == "&s":
                            if int(token[1]) != len(programs):
                                print(f"{mce}: violation of the numbering order")
                                exit(1)

                            program_index = int(token[1])

                        elif token[2] == "&e":
                            program_index = -1

                    case "r":
                        list_of_programs = list(map(int, token[1:token.index(';')]))
                        # TODO use Exceptions
                        if max(list_of_programs) >= len(programs):
                            print(f"{mce}: program {max(list_of_programs)} is undefined")
                            print(f"{mce}: program index in {rtc} string is not a program")
                            exit(1)

                        else:
                            for num in list_of_programs:
                                run(programs[num])

                    case "x":
                        for program in programs:
                            run(program)
                    # TODO use Exceptions
                    case _:
                        print(f"{mce}: .{token[0]} specifier hasn't been defined")
                        exit(1)

    maider(source_lines)


main(input())
