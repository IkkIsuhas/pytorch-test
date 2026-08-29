import torch

marks = torch.tensor([
    [85,90,78],
    [70,88,95],
    [92,76,89]
])

print("Marks: ")
print(marks)

print(f"\n Average Marks:\n {marks.float().mean()}")
print(f"Average Marks for each subject:\n {marks.float().mean(dim=0)}")
print(f"Average Marks for each student:\n {marks.float().mean(dim=1)}")
print(f"Highest marks: \n {torch.max(marks)}")
print(f"Lowest marks: {torch.min(marks)}")