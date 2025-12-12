import cv2
import numpy as np

def segment_captcha(image_bytes: bytes):
    np_arr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_GRAYSCALE)

    _, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(thresh, connectivity=8)

    components = []
    char_imgs = []

    for i in range(1, num_labels):
        x, y, w, h, area = stats[i]

        if area < 50:
            continue  
        components.append((x, y, w, h))
        char = thresh[y:y+h, x:x+w]
        char = cv2.resize(char, (28, 28))

        char_imgs.append(char)

    sorted_chars = [
        img
        for (_, img) in sorted(
            zip(components, char_imgs),
            key=lambda x: x[0][0]  
        )
    ]

    return sorted_chars
