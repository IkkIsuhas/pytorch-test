## Creating random valued tensor with 5 rows and 3 columns

import torch
x = torch.rand(5,3)
print(f"Original tensor:\n {x}")
print(f"Size of tensor: {x.shape}")
print(f"Dimension: {x.ndim}")
print(f"Datatype of the tensor:{x.dtype}")