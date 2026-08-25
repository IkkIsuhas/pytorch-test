## convert [12] into [3,4]
import torch 
x = torch.arange(1,13)
print(x)
y = x.reshape(3,4)
print(y)