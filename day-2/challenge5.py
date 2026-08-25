## Reshpaing the tensor to [12,1] using unsqueeze
import torch

x = torch.arange(1,13)
y = x.unsqueeze(1)
print(f"Original tensor:\n {x}")
print(f"shape of original tensor:{x.shape}")
print(f"Unsqueeze tensor:\n {y}")
print(f"Shape of unsqueeze tensor:{y.shape}")