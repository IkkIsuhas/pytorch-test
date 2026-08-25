## create a tensor and print it's shape, dimension and dtype
import torch 

x = torch.tensor([10,20,30,40,50])
print(f"Original tensor: {x}")
print(f"Shape of the tensor: {x.shape}")
print(f"Dimension of the tensor: {x.ndim}")
print(f"Data type of the tensor: {x.dtype}")