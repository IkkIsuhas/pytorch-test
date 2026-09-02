import torch
import pandas as pd
from torch.utils.data import Dataset, DataLoader

class CustomerData(Dataset):

    def __init__(self,data):
        self.data = pd.read_csv(data)

    def __len__(self):
        return len(self.data)

    def __getitem__(self,index):
        features = self.data.iloc[index,:-1].values
        labels = self.data.iloc[index,-1]

        features = torch.tensor(features, dtype=torch.float32)
        labels = torch.tensor(labels, dtype=torch.long)

        return features, labels

dataset = CustomerData("../customers.csv")

loader = DataLoader(
    dataset,
    batch_size=4,
    shuffle=True
)

x,y = dataset[0]

print(f"Length of the dataset: {len(dataset)}")
print(f"Value of X: {x}")
print(f"Value of Y: {y}")

for i in range(len(dataset)):
    print(dataset[i])