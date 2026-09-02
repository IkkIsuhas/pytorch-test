# import torch

# customers = torch.tensor([
#     [25, 30000, 3, 1],
#     [35., 50000., 5., 4.],
#     [42., 70000., 8., 7.],
#     [28., 40000., 2., 0.]
# ])

# print(customers)
# print(customers.shape)
# print(customers[0,1])

import torch

t = torch.tensor([25.,25000.,3.,1.])
print(t)
m = t.float().mean(dim=0)
s = t.std(dim=0)
t_scaled = (t-m)/s
print(t_scaled)