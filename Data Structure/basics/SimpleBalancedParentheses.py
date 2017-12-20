from stack import Stacks


def simple_balanced_parenthesis(symbolString):
    s = Stacks()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        if symbolString[index] == '[':
            s.push(']')
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()

        index += 1

    if s.is_empty() and balanced:
        return True
    else:
        return False


def par_checker(symbolString):
    s = Stacks()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in '[{(':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False

        index += 1

    if s.is_empty() and balanced:
        return True
    else:
        return False


def matches(opening, close):
    opens = '{[('
    closes = '}])'
    return opens.index(opening) == closes.index(close)


print(par_checker('{{([][])}()}'))
print(par_checker('[{()]'))
print(simple_balanced_parenthesis('[[[[][]]]'))


