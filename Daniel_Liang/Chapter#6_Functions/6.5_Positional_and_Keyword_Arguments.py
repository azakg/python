
def nPrint(message, n):
    for i in range(n):
        print(message)
def main():
    nPrint('Positional Argument', 3)
    nPrint(n = 3, message = 'Keyword Argument')

main()
