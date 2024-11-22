from PIL import Image
import numpy as np

def dhash_pil(image, hash_size=8):
    try:
        img = image.convert("L").resize((hash_size + 1, hash_size), Image.ANTIALIAS)
        diff = np.array(img)[:, 1:] > np.array(img)[:, :-1]
        hash_value = sum([2**i for (i, v) in enumerate(diff.flatten()) if v])
        return f"{hash_value:0{hash_size**2//4}x}"  # Convert to hex string
    except Exception as e:
        print(f"Error dhash_pil: {e}")
        return None

def get_image(image_path):
    try:
        with Image.open(image_path) as img:
            return img
    except Exception as e:
        print(f"Error get_image: {e}")
        return None