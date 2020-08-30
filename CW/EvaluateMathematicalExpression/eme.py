# Evaluate mathematical expression

#  Instructions
# Given a mathematical expression as a string you must return the result as a number.
#
# Numbers
# Number may be both whole numbers and/or decimal numbers. The same goes for the returned result.
#
# Operators
# You need to support the following mathematical operators:
#
# Multiplication *
# Division / (as true division)
# Addition +
# Subtraction -
# Operators are always evaluated from left-to-right, and * and / must be evaluated before + and -.
#
# Parentheses
# You need to support multiple levels of nested parentheses, ex. (2 / (2 + 3.33) * 4) - -6
#
# Whitespace
# There may or may not be whitespace between numbers and operators.
#
# An addition to this rule is that the minus sign (-) used for negating numbers and parentheses will never be
# separated by whitespace. I.e., all of the following are valid expressions.
#
# 1-1    // 0
# 1 -1   // 0
# 1- 1   // 0
# 1 - 1  // 0
# 1- -1  // 2
# 1 - -1 // 2
#
# 6 + -(4)   // 2
# 6 + -( -4) // 10
# And the following are invalid expressions
#
# 1 - - 1    // Invalid 1- - 1     // Invalid 6 + - (4)  // Invalid 6 + -(- 4) // Invalid Validation You do not need
# to worry about validation - you will only receive valid mathematical expressions following the above rules.


import operator

OP_DICT = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


def getTokens(expression):
    tokens = []
    stack = []
    op = dict()
    cl = dict()

    i = 0
    while i < len(expression):
        # whitespace
        if expression[i] == ' ':
            i += 1
            continue
        # digit
        if expression[i].isdigit():
            j = i
            while i + 1 < len(expression) and (expression[i + 1].isdigit() or expression[i + 1] == '.'):
                i += 1
            # add num
            tokens.append(float(expression[j: i + 1]))
        # parentheses
        else:
            if expression[i] == '(':
                stack.append(len(tokens))
            if expression[i] == ')':
                j = len(tokens)
                op[j] = stack.pop()
                cl[op[j]] = j
            tokens.append(expression[i])
        i += 1
    return tokens, op, cl


def calc(e):
    tokens, op, cl = getTokens(e)

    def eval_muldiv(tokens):
        v, o = 1, '*'
        for token in tokens:
            if isinstance(token, float):
                v = OP_DICT[o](v, token)
            else:
                o = token
        return v

    def dfs(s, e):
        x = s
        tokens_no_par = []
        while x <= e:
            if tokens[x] == '(':
                v = dfs(x + 1, cl[x] - 1)
                tokens_no_par.append(v)
                x = cl[x]
            else:
                tokens_no_par.append(tokens[x])

            x += 1
        tokens_no_neg = []
        x = 0
        while x < len(tokens_no_par):
            if tokens_no_par[x] != '-':
                tokens_no_neg.append(tokens_no_par[x])
            else:
                if x > 0 and isinstance(tokens_no_par[x - 1], float):
                    tokens_no_neg.append('-')
                else:
                    j = x
                    while not isinstance(tokens_no_par[x], float):
                        x += 1
                    n_neg = x - j
                    v = tokens_no_par[x] * ((-1) ** (n_neg % 2))
                    tokens_no_neg.append(v)
            x += 1
        idx_addsub = [-1]
        for idx, token in enumerate(tokens_no_neg):
            if token == '+' or token == '-':
                idx_addsub.append(idx)

        v, o = 0, '+'
        for i in range(1, len(idx_addsub)):
            j, k = idx_addsub[i - 1], idx_addsub[i]
            v1 = eval_muldiv(tokens_no_neg[j + 1: k])
            v = OP_DICT[o](v, v1)
            o = tokens_no_neg[k]

        v = OP_DICT[o](v, eval_muldiv(tokens_no_neg[idx_addsub[-1] + 1:]))
        return v

    return dfs(0, len(tokens) - 1)


print(calc("-7 * -(6 / 3)"))
