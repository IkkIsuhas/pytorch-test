import torch

data = torch.tensor([
    [22., 25000., 2., 0.],
    [35., 52000., 6., 3.],
    [41., 68000., 9., 8.],
    [29., 41000., 4., 2.],
    [52., 90000., 12., 10.],
    [24., 28000., 3., 1.],
    [38., 61000., 7., 5.],
    [45., 75000., 10., 9.]
])

labels = torch.tensor([
    0,
    1,
    1,
    0,
    1,
    0,
    1,
    1
])

shape1 = data.shape
shape2 = labels.shape
avg_data = data.float().mean(dim=0)
highest_salary = data[:,1]
print(f"Highest salary: {highest_salary}")
index = torch.argmax(data[:,1])
print(f"Highest salary customer:\n {data[index]}")
active = data[:,2]
max_a = torch.argmax(active)
print(f"customer visited the website the most:\n {data[max_a]}")
# print(f"shape:\n{shape1}\n{shape2}")
# print(avg_data)