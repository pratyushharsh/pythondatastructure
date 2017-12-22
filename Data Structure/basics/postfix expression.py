from stack import Stacks


def infix_to_postfix(infixexpr):
    # creating a dictionary to store the precedence order
    precedence_order = {"*": 3,
                        "/": 3,
                        "+": 2,
                        "-": 2,
                        "(": 1}

    opstack = Stacks()
    post_fix_list = []
    token_list = infixexpr.split()

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            post_fix_list.append(token)
        elif token == '(':
            opstack.push(token)
        elif token == ')':
            top_token = opstack.pop()
            while top_token != '(':
                post_fix_list.append(top_token)
                top_token = opstack.pop()
        else:
            while (not opstack.is_empty()) and \
                    (precedence_order[opstack.peek()] >= precedence_order[token]):
                    post_fix_list.append(opstack.pop())
            opstack.push(token)

    while not opstack.is_empty():
        post_fix_list.append(opstack.pop())

    return " ".join(post_fix_list)


print(infix_to_postfix("A * B + C * D"))
print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))


def post_fix_eval(postfixexpr):
    operand_stack = Stacks()
    token_list = postfixexpr.split()

    for token in token_list:
        if token in "0123456789":
            operand_stack.push(int(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)

    return operand_stack.pop()


def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    elif op == "/":
        return op1 / op2


print(post_fix_eval('7 8 + 3 2 + /'))