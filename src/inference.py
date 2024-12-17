from model import load_model
import torch

model = load_model()

def run_inference(input_data):
    input_tensor = torch.tensor(input_data).float().unsqueeze(0)
    with torch.no_grad():
        output = model(input_tensor)
    return output.tolist()
