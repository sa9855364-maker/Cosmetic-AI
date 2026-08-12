import os
import cv2
import numpy as np

def generate_face_masks(faces_dir, masks_dir):
    os.makedirs(masks_dir, exist_ok=True)
    files = [f for f in os.listdir(faces_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    print(f"Generating segmentation masks for {len(files)} images...")
    
    for filename in files:
        img_id = os.path.splitext(filename)[0]
        img_bgr = cv2.imread(os.path.join(faces_dir, filename))
        if img_bgr is None: continue
        
        h, w, _ = img_bgr.shape
        mask = np.zeros((h, w, 3), dtype=np.uint8)
        mask[:, :] = [50, 50, 50] # Skin
        
        # Nose mask
        cv2.ellipse(mask, (w//2, int(h*0.55)), (int(w*0.12), int(h*0.18)), 0, 0, 360, (0, 255, 0), -1)
        # Lips mask
        cv2.ellipse(mask, (w//2, int(h*0.75)), (int(w*0.18), int(h*0.08)), 0, 0, 360, (0, 0, 255), -1)
        # Eyes mask
        cv2.ellipse(mask, (int(w*0.35), int(h*0.42)), (int(w*0.09), int(h*0.05)), 0, 0, 360, (255, 0, 0), -1)
        cv2.ellipse(mask, (int(w*0.65), int(h*0.42)), (int(w*0.09), int(h*0.05)), 0, 0, 360, (255, 0, 0), -1)
        
        cv2.imwrite(os.path.join(masks_dir, f"{img_id}.png"), mask)
        
    print(f"✅ Created segmentation masks in {masks_dir}")

if __name__ == '__main__':
    generate_face_masks('./processed/faces', './processed/masks')
