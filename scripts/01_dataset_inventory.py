import os
import pandas as pd
from PIL import Image

def scan_dataset(raw_dir):
    inventory = []
    print(f"Scanning raw datasets in: {raw_dir}")
    
    if not os.path.exists(raw_dir):
        print(f"Directory {raw_dir} does not exist.")
        return

    for root, dirs, files in os.walk(raw_dir):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in ['.jpg', '.jpeg', '.png', '.bmp', '.webp']:
                file_path = os.path.join(root, file)
                try:
                    with Image.open(file_path) as img:
                        width, height = img.size
                        mode = img.mode
                except Exception:
                    width, height, mode = None, None, None
                
                rel_path = os.path.relpath(file_path, raw_dir)
                dataset_name = rel_path.split(os.sep)[0]
                
                inventory.append({
                    'dataset_name': dataset_name,
                    'file_name': file,
                    'relative_path': rel_path,
                    'extension': ext,
                    'width': width,
                    'height': height,
                    'color_mode': mode
                })

    df = pd.DataFrame(inventory)
    output_csv = os.path.join(os.path.dirname(raw_dir), 'dataset_inventory.csv')
    df.to_csv(output_csv, index=False)
    print(f"✅ Saved inventory to {output_csv}")

if __name__ == '__main__':
    scan_dataset('./raw_datasets')
