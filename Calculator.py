def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n2-n1

def division(n1,n2):
    return n2/n1

def multiplication(n1,n2):
    return n1*n2

operations = {
    "+": add ,
    "-": subtract,
    "*": multiplication,
    "/": division,
}

n1 = int(input("Enter first number: "))

n2 = int(input("Enter second number: "))

print("Choose the operation you want: ")

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the line above: ")


calculation_function = operations[operation_symbol]
answer = calculation_function(n1, n2)
print(f"{n1} {operation_symbol} {n2} = {answer}")

print("Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.")
should_continue = input("Type 'y' or 'n': ")
if should_continue == "y":
    n1 = answer
    n2 = int(input("Enter next number: "))
    operation_symbol = input("Pick an operation from the line above: ")
    calculation_function = operations[operation_symbol]
    second_answer = calculation_function(n1, n2)
    print(f"{n1} {operation_symbol} {n2} = {second_answer}")
else:
    print("Starting a new calculation...")
    print("------------------------------")
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    operation_symbol = input("Pick an operation from the line above: ")
    calculation_function = operations[operation_symbol]
    answer = calculation_function(n1, n2)
    print(f"{n1} {operation_symbol} {n2} = {answer}")  