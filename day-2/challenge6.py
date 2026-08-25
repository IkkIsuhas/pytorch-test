## Reshape tensor to [4,1] using squeeze
import torch
x = torch.tensor([
    [1],
    [2],
    [3],
    [4]
])
y = x.squeeze(1)
print(f"Original tensor:\n {x}")
print(f"Shape of the original tensor: {x.shape}")
print(f"Squeeze tensor: {y}")
print(f"Shape of squeeze tensor: {y.shape}")