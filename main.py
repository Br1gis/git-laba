print('Something is started...')
a = int(input("Enter 1 num: "))
b = int(input("Enter 2 num: "))
operation = input("Enter operation: ")
if operation == '+':
    print(a + b)
elif operation == '-':
    print(a - b)
elif operation == '*':
    print(a * b)
elif operation == '/':
    if b != 0:
        print(a / b)
    else:
        print('Scha kak dam po rukam')

