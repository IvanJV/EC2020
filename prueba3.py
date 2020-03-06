
def and_fun(expr):
    k = expr.index('&')
    i = 1
    tmp = expr[0]
    while i < k:
        tmp = tmp and expr[i]
        i += 1
    expr[k] = tmp

    return expr[k:]

def or_fun(expr):
    k = expr.index('|')
    i = 1
    tmp = expr[0]
    while i < k:
        tmp = tmp or expr[i]
        i += 1
    expr[k] = tmp

    return expr[k:]

def not_fun(expr):
    k = expr.index('!')
    expr[k] = not expr[k-1]
    expr.pop(k-1)
    return expr

def ParseBoolean(expression):
    expression = expression.replace('(','').replace(')','').replace(',','')
    bols = expression.replace('t','').replace('f','')

    expression = list(expression)
    expression.reverse()

    bols = list(bols)
    bols.reverse()
    
    i = 0
    for i in range(len(expression)):
        if expression[i] == 't': expression[i] = True
        elif expression[i] == 'f': expression[i] = False

    expr = expression
    
    for bol in bols:
        if bol == '!': expr = not_fun(expr)
        elif bol == '|': expr = or_fun(expr)
        elif bol == '&': expr = and_fun(expr)

    return expr[0]

expression = '|(!(t),&(t,t,t))'
print(ParseBoolean(expression))