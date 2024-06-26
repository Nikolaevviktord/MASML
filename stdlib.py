class Namespace:
    def __init__(self, name, *methods):
        self.name = name
        self.names = {}
        for i in methods:
            self.names[f'{i[0]}'] = i[1]


class TypeNamespace:
    def __init__(self, name, *methods):
        self.name = name
        self.types = {}
        for i in methods:
            self.types[f'{i[0]}'] = f'{i[1]}'


def import_stdlib(mode, code):
    containers = TypeNamespace('containers',
                               ['queue', 'q'],
                               ['list', 'l'])

    strtypes = TypeNamespace('strtypes',
                             ['strtype', 'y'],
                             ['prog', 'p'],
                             ['var', 'v'],
                             ['con', 'c'],
                             ['list', 'l'],
                             ['for', 'f'],
                             ['deinit', 'd'],
                             ['arthm', 'a'],
                             ['run', 'r'],
                             ['while', 'w'],
                             ['if', 'i'],
                             ['else', 'e'],
                             ['clear', 'z'],
                             ['save', 's'],
                             ['using', 'u'],
                             ['run_all', 'x'],
                             ['type', 't'],
                             ['hide', 'h'],
                             ['operator', 'o'],
                             ['import', 'm'],
                             ['namespace', 'n'])

    types = Namespace('types',
                      ['int', '#i'],
                      ['bool', '#b'])

    hides = Namespace('hides',
                      ['start', '&s'],
                      ['end', '&e'],
                      ['in', '*i'],
                      ['out', '*o'])

    operators = Namespace('operators',
                          ['_a_[_b_]', '_a_._b_'])


    if (mode == '&'):
        for i, j in containers.types.items():
            code = code.replace(i, j)
        for i, j in strtypes.types.items():
            code = code.replace(i, j)
        for i, j in types.names.items():
            code = code.replace(i, j)
        for i, j in hides.names.items():
            code = code.replace(i, j)
        while '[' in code:
            indo = code.index('[')
            indc = code.index(']')
            name_inside = code[indo+1:indc]
            code = code.replace(code[indo:indc+1], f'^{name_inside}')
    return code
