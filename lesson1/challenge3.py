## creating a custom size tensor of 3 rows, 4 columns
import torch

x = torch.tensor([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(f"Original tensor \n: {x}")
print(f"Shape of the tensor: {x.shape}")