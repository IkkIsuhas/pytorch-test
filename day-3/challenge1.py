import torch

a = torch.tensor([10, 20, 30, 40])
b = torch.tensor([1, 2, 3, 4])

def add(a,b):
    return f"Addition of 2 tensor is:\n {a+b}"

def sub(a,b):
    return f"Substraction of 2 tensor is:\n {a-b}" 

def mul(a,b):
    return f"Multiplication of 2 tensor is:\n {a*b}"

def div(a,b):
    return f"Divide of 2 tensor is:\n {a/b}"

while True:
    choice = input("Enter your choice: ")
    if choice.lower() == "exit":
        break
    elif choice == "+":
        print(add(a,b))
    elif choice == "-":
        print(sub(a,b))
    elif choice == "*":
        print(mul(a,b))
    elif choice == "/":
        print(div(a,b))
    else:
        print( 'Error')