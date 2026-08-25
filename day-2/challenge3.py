## convert the original tensor into [2,6]
import torch
x = torch.arange(1,13)
y = x.reshape(2,6)
print(f"Original tensor: {x}")
print(f"Reshaped tensor:\n {y}")