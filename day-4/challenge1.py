import torch

a = torch.tensor([[1,2,3],
                 [4,8,6]])
b = torch.tensor([10,20,30])

result = a+b
print(result)
print(torch.max(a))
print(torch.argmax(a,dim=1))
print(torch.argmax(b))
print(torch.argmax(result))