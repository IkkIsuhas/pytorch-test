## Sum of the 2D tensor in 0 and 1 dimension
import torch

x = torch.tensor([
    [1, 2, 3],
    [4, 5, 6]
])

print(f"Sum of vaules in 2D tensor{x.sum()}")
print(f"Sum of 2D tensor in dimension=0: {x.sum(dim=0)}") # columns-wise sum
print(f"Sum of 2D tensor in dimension=1: {x.sum(dim=1)}") # row-wise sum