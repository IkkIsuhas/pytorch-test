import torch 
from torch.utils.data import Dataset, DataLoader

data = torch.tensor([
    [22., 25000., 2., 0.],
    [35., 52000., 6., 3.],
    [41., 68000., 9., 8.],
    [29., 41000., 4., 2.],
    [52., 90000., 12., 10.],
    [24., 28000., 3., 1.],
    [38., 61000., 7., 5.],
    [45., 75000., 10., 9.],
    [31., 47000., 5., 3.],
    [27., 35000., 3., 1.],
    [49., 82000., 11., 8.],
    [36., 58000., 6., 4.]
])

labels = torch.tensor([
    0, 1, 1, 0,
    1, 0, 1, 1,
    0, 0, 1, 1
])

class sample(Dataset):

    def __init__(self):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self,index):
        features = data[index,:-1]
        labels = labels[index,-1]