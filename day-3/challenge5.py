import torch

a = torch.tensor([
    [1, 2],
    [3, 4]
])

b = torch.tensor([
    [5, 6],
    [7, 8]
])

print(f"Multiplication: \n{a*b}")
print(f"Matrix Multiplication: \n{torch.matmul(a,b)}") ## a @ b