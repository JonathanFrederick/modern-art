import random
from math import *
# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.

def rxy():
    return random.choice(['x', 'y'])

def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    # expr1 = lambda x, y: (x + y)/2
    # expr2 = lambda x, y: (x - y)/2
    # expr3 = lambda x, y: random.choice([x, y])*random.choice([x, y])
    # expr4 = lambda x, y: abs(random.choice([x, y]))**random.choice([x, y])
    # expr5 = lambda x, y: abs(random.choice([x, y]))
    # return random.choice([expr1, expr2, expr3, expr4, expr5])
    string = 'lambda x, y: '
    expr1 = 'exp('
    expr2 = 'cos('
    expr3 = 'sin('
    expr4 = 'abs('
    expr5 = 'atan('
    expr6 = 'tan('

#    expr8 = rxy()+'*'+rxy()
    for i in range(5):
        string += random.choice([expr1, expr2, expr3, expr4, expr5, expr6])
        string += rxy()+'*'

    string += random.choice([expr1, expr2, expr3, expr4, expr5, expr6])+rxy()+'))))))'
    return eval(string)




def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr(x, y)
