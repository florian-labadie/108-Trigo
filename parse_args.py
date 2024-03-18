import sys
from math import sqrt

function = sys.argv[1]
args = sys.argv[2:]

def check_fct(fct):
    if fct == None:
        return None
    if fct != "COS" and fct != "SIN" and fct != "COSH" and fct != "SINH" and fct != "EXP":
        return None
    return fct

def parse_args():
    if function == None or args == None:
        return 84
    size = sqrt(len(args))
    if size - int(size) != 0:
        return 84
    matrix = [[int(args[j]) for j in range(i, i + int(size))] for i in range(0, len(args), int(size))]
    return check_fct(function), matrix
