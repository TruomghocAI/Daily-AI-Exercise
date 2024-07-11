import torch
import torch.nn as nn

class Sigmoid(nn.Module):
    def __init__(self):
        super(Sigmoid, self).__init__()
    
    def forward(self,x):
        return 1/ (1 + torch.exp(-x))

class Relu(nn.Module):
    def __init__(self):
        super(Relu, self).__init__()
    def forward(self,x):
        return torch.relu(x)
    
if __name__ == '__main__':
    relu = Relu()
    x = torch.tensor([1,-5,1.5,2.7,-5])
    output = relu(x)
    print(output)