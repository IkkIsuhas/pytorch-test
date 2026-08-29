## day-4 challenge 

import torch

scores = torch.tensor([
    [80., 90., 70.],
    [60., 75., 95.],
    [88., 92., 85.]
])

print(f"Shape of the tensor:\n{scores.shape}")
print(f"Overall average of score:\n{scores.float().mean()}")
print(f"Average score of each student: \n{scores.float().mean(dim=1)}")
print(f"Average score of each subjects: \n{scores.float().mean(dim=0)}")
avg_score = scores.float().mean(dim=0)
print(avg_score)
print(f"Highest average score of the subject: \n{torch.argmax(avg_score)}")
