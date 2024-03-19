from parse_args import parse_args
from trigo import trigo

if __name__ == '__main__':
    try:
        function, matrix = parse_args()
        if function == None or matrix == 84:
            exit(84)
        if trigo(function, matrix) == 84:
            exit(84)
    except Exception as e:
        exit(84)
