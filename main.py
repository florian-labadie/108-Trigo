from parse_args import parse_args
from trigo import trigo

if __name__ == '__main__':
    try:
        function, args = parse_args()
        if function == None or args == 84:
            exit(84)
        if trigo(args) == 84:
            exit(84)
    except Exception as e:
        exit(84)


