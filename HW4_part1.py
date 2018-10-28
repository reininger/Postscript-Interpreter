#programmer: Reid Reininger(charles.reininger@wsu.edu)
#date: 10/24/18
#desc: (intended for Unix/Linux)

opstack = []
dictstack = [{}]

def opPop():
    return opstack.pop()

def opPush(value):
    return opstack.append(value)

def dictPop():
    return dictstack.pop()

def dictPush():
    return dictstack.append({})

def define(name, value):
    dictstack[-1][name] = value

def lookup(name):
    for x in reversed(dictstack):
        for key in x:
            if key == name:
                return x[key]
    else:
        print('error: name not found')
