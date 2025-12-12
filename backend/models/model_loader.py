import torch
import os
from .model import CaptchaCNN

model = CaptchaCNN()

model_path = os.path.join(os.path.dirname(__file__), "captcha_model.pth")

model.load_state_dict(torch.load(model_path, map_location="cpu"))
model.eval()
