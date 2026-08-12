import os
import cv2
import numpy as np

def align_and_crop_ffhq(img_rgb, target_size=(512, 512), margin=0.2):
    """
    Phase 2 FFHQ Processing: Crop face with margin and resize to 512x512.
    """
    h, w, _ = img_rgb.shape
    cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cascade_path)
    gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    
    if len(faces) == 0:
        side = min(h, w)
        x1, y1 = (w - side) // 2, (h - side) // 2
        cropped = img_rgb[y1:y1+side, x1:x1+side]
    else:
        x, y, fw, fh = faces[0]
        mx, my = int(fw * margin), int(fh * margin)
        x1, y1 = max(0, x - mx), max(0, y - my)
        x2, y2 = min(w, x + fw + mx), min(h, y + fh + my)
        cropped = img_rgb[y1:y2, x1:x2]
        
    return cv2.resize(cropped, target_size, interpolation=cv2.INTER_CUBIC)

def process_ffhq_folder(input_dir, output_dir, limit=5000):
    os.makedirs(output_dir, exist_ok=True)
    files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))][:limit]
    
    count = 0
    for filename in files:
        img_bgr = cv2.imread(os.path.join(input_dir, filename))
        if img_bgr is None: continue
        
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        aligned = align_and_crop_ffhq(img_rgb, target_size=(512, 512))
        
        save_name = f"{count+1:06d}.jpg"
        cv2.imwrite(os.path.join(output_dir, save_name), cv2.cvtColor(aligned, cv2.COLOR_RGB2BGR))
        count += 1
        
    print(f"✅ Processed {count} images to 512x512 in {output_dir}")

if __name__ == '__main__':
    process_ffhq_folder('./raw_datasets/FFHQ', './processed/faces', limit=5000)
