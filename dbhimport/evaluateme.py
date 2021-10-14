import math

def evaluateme(cmd):
    try:
        print(eval(cmd[1]))
    except:
        print(str(cmd[1])+ ": Cannot be evaluated.") 
    return