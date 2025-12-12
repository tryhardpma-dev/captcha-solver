import torch
from PIL import Image
import io
from models.model import model

def solve_captcha(image_bytes: bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image = image.resize((80, 40))

    tensor = torch.tensor(
        torch.ByteTensor(torch.ByteStorage.from_buffer(image.tobytes()))
    )
    tensor = tensor.view(40, 80, 3).permute(2, 0, 1).float() / 255.0
    tensor = tensor.unsqueeze(0)

    with torch.no_grad():
        output = model(tensor)
        _, predicted = torch.max(output, 1)

    return str(predicted.item())
