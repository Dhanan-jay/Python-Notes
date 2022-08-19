first = input("Enter the First number : ")

second = input("Enter the Second Number : ")

operator = input("Enter the Operators (+ , - , * , /) : ")

first = int(first)
second = int(second)

if operator == '+':
    print("The Sum is : ", first + second)

elif operator == '-':
    print(first - second)

elif operator == '*':
    print(first * second)

elif operator == '/':
    print(first / second)

else:
    print("!! Invalied Number !!")
