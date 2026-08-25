## print the shape and dimension of the tensor
import torch 

x = torch.tensor([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(f"Original tensor: {x}")
print(f"Shape of the tensor:{x.shape}")
print(f"Dimension of the tensor:{x.ndim}")