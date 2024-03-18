from trigo import parse_args
from trigo import trigo

if __name__ == '__main__':
    try:
        args = parse_args()
        if args == 84:
            exit(84)
        if trigo(args) == 84:
            exit(84)
    except Exception as e:
        exit(84)


