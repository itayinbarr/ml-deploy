import torch
import os
import torch.nn as nn

class CustomModel(nn.Module):
    def __init__(self):
        super().__init__()
        # Example: a simple linear layer
        self.fc = nn.Linear(3, 1)

    def forward(self, x):
        return self.fc(x)

def load_model(weights_path=None):
    if weights_path is None:
        weights_path = os.getenv('MODEL_WEIGHTS_PATH', 'src/weights/model_weights.pt')
    model = CustomModel()
    model.load_state_dict(torch.load(weights_path, map_location='cpu'))
    model.eval()
    return model
