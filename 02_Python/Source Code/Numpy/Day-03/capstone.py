import numpy as np
from report import generate_report

rng = np.random.default_rng(42)

gray = rng.integers(0, 256, size=(256, 256), dtype=np.uint8)
colour = rng.integers(0, 256, size=(256, 256, 3), dtype=np.uint8)

row_grad = np.linspace(0, 255, 256)[:, np.newaxis]
col_grad = np.linspace(0, 255, 256)[np.newaxis, :]
gradient = ((row_grad + col_grad) / 2).astype(np.uint8)

def adjust_brightness(img, delta):
    adjusted = img.astype(np.int16) + delta
    return np.clip(adjusted, 0, 255).astype(np.uint8)

brighter = adjust_brightness(gray, 50)
darker = adjust_brightness(gray, -50)

def adjust_contrast(img, factor):
    adjusted = 128 + factor * (img.astype(np.float32) - 128)
    return np.clip(adjusted, 0, 255).astype(np.uint8)

high_contrast = adjust_contrast(gray, 1.5)
low_contrast = adjust_contrast(gray, 0.5)

adjustment = np.array([[[30, 0, -20]]])
colour_adjusted = np.clip(colour.astype(np.int16) + adjustment, 0, 255).astype(np.uint8)

weights = np.array([0.299, 0.587, 0.114])
gray_from_colour = (colour * weights).sum(axis=-1).astype(np.uint8)

binary = np.where(gray > 128, 255, 0).astype(np.uint8)
white_pct = (binary == 255).mean() * 100

inverted = (255 - gray).astype(np.uint8)

def box_blur(img):
    blurred = np.zeros_like(img, dtype=float)
    blurred[1:-1, 1:-1] = (
        img[0:-2, 0:-2] + img[0:-2, 1:-1] + img[0:-2, 2:] +
        img[1:-1, 0:-2] + img[1:-1, 1:-1] + img[1:-1, 2:] +
        img[2:,   0:-2] + img[2:,   1:-1] + img[2:,   2:]
    ) / 9.0
    return blurred.astype(np.uint8)

blurred_gray = box_blur(gray)

flip_h = gray[:, ::-1]
flip_v = gray[::-1, :]
flip_both = gray[::-1, ::-1]

roi = gray[64:192, 64:192]
small = gray[::2, ::2]

image_report = generate_report(gray, brighter, blurred_gray, white_pct)
print(image_report)