# adding equation
def add(x, y):
    return x + y

#subtracting equation
def sub(x, y):
    return x - y
#multiply equatin
def times(x, y):
    return x * y

#dividing equation
def div(x, y):
    return x / y

#to the power of equation
def powerof(x ,y):
    return x ** y


print('select operation:')
print('1. Add')
print('2. subtract')
print('3. multiply')
print('4. divide')
print('5. raise the number to the power of')

choice=input('enter 1,2,3,4')

if choice == '1':
    answer=add(num1, num2)
    print(num1, ' + ', num2, ' = ',asnwer)
elif choice == '2':
    answer=subtract(num1, num2)
    print(num1, ' - ',num2, ' = ',answer
elif choice == '3':
          answer=multiply(num1, num2)
              print(num1, ' * ', num2, ' = ',answer)
elif choice == '4':
          answer=divide(num1, num2)
          print(num1, ' / ', num2 ' = ', answer)
elif choice == '4':
          answer=power(num1, num2)
          print(num1

num1 = float(input('Enter your first number: '))

num2 = float(input('Enter your second number: '))

print(num1, '+', num2, '=', add(num1, num2))


