import torch 
import time

x = torch.tensor([5, 10, 15, 20, 25])
start = time.perf_counter()
print(f"Sum of tensor: \n{x.sum()}")
end = time.perf_counter()
print(f"Time {end-start} MS")
print(f"Mean of the tensor: \n{x.float().mean()}")
print(f"Minimum value: \n{x.min()}")
print(f"Maximum value: \n{x.max()}")