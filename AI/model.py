import torch
import torch.nn as nn
import torch.nn.functional as F
import os


class LinearQNet(nn.Module):

    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.linear1 = nn.Linear(input_size, hidden_size)
        self.linear2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        """Pythorch forward function. (prediction)"""
        x = F.relu(self.linear1(x))
        x = self.linear2(x)
        return x

    def save(self, file_name='model.pth'):
        """Save model"""
        model_folder = './model'
        if not os.path.exists(model_folder):    # if model folder does not exist
            os.makedirs(model_folder)   # we create the folder

        file_name = os.path.join(model_folder, file_name)  # creat path to the model (for save)
        torch.save(self.state_dict(), file_name)    # save the model
