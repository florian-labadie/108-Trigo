import sys

args = sys.argv[1:]

def parse_args():
    tab = []
    if (len(args) == 0 or len(args) % 2 != 0):
        return 84
    for i in range(len(args)):
        tab.append([int(x) for x in args[i].split('*')])
    return tab
