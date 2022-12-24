

from calculatorlogo import logo
print("WELCOME TO CALCULATOR IN PYTHON")
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def divide(n1,n2):
    return n1/n2
def multiply(n1,n2):
    return n1*n2

operation={
    "+":add,
    "*":multiply,
    "-":subtract,
    "/":divide
}

def calculator():
    print(logo)
    num1=float(input("What is the first number "))
        # num2=int(input("Enter the second number\n "))
    for symbol in operation:
        print(symbol)
    should_continue=False

    while not should_continue:
        operational_symbols=(input("Insert the opration you are willing to perform "))
        num2=float(input("Enter the next number "))
        computational_operation=operation[operational_symbols]
        answer=computational_operation(num1,num2)

        print(f"{num1} {operational_symbols} {num2} = {answer}")

        continuation=input("Type yes if YES would like to continue, or type NO to start a new calculation? ")
        if continuation=="YES".lower():
            num1=answer
        else:
            should_continue=True
            calculator()
calculator()

   

    # if continuation=="yes":
    #     # print(f"{num1} {operational_symbols} {num2} = {first_answer}")
    #     operational_symbols=(input("Insert the opration you are willing to perform "))
    #     num3=int(input("Enter the second number"))
    #     computational_operation=operation[operational_symbols]
    #     second_answer=computational_operation(answer,num3) # or second_answer=computational_operation(computational_operation(num1,num2),num3)
    #     print(f"{answer} {operational_symbols} {num3} = {second_answer}")
    # else:
    #     should_continue=True
