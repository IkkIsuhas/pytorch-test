## unsqueeze the original tensor to [1, 12]
import torch 

x = torch.arange(1,13)
print(F"Original tensor: {x}")
print(F"Size of the tensor: {x.shape}")
y = x.unsqueeze(0)
print(f"Unsqueeze tensor: {y}")
print(f"Shape tensor: {y.shape}")