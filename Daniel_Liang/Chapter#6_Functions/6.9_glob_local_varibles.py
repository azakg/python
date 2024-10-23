globalVar = 1
def f1():
    # global localVar
    localVar = 2
    print(globalVar)
    print(localVar)

f1()
print(globalVar)
print(localVar)