import torch
from .segmentation import segment_captcha
from backend.models.model_loader import model

CLASSES = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def predict_char(img28):
    tensor = torch.tensor(img28, dtype=torch.float32).unsqueeze(0).unsqueeze(0) / 255.0

    with torch.no_grad():
        pred = model(tensor).argmax(1).item()

    return CLASSES[pred]

def solve_captcha(image_bytes):
    chars = segment_captcha(image_bytes)
    return "".join(predict_char(ch) for ch in chars)
