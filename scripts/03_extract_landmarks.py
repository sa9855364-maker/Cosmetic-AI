import os
import json
import cv2
import mediapipe as mp

LANDMARK_GROUPS = {
    "lips": [61, 185, 40, 39, 37, 0, 267, 269, 270, 409, 291, 375, 321, 405, 314, 17, 84, 181, 91, 146, 61],
    "nose": [1, 2, 98, 327, 168, 197, 5, 4, 275],
    "left_eye": [33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161, 246, 33],
    "right_eye": [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398, 362],
    "jawline": [10, 338, 297, 332, 284, 251, 389, 356, 454, 323, 361, 288, 397, 365, 379, 378, 400, 377, 152, 148, 176, 149, 150, 136, 172, 58, 132, 93, 234, 127, 162, 21, 54, 103, 67, 109, 10]
}

def extract_landmarks(faces_dir, landmarks_dir):
    os.makedirs(landmarks_dir, exist_ok=True)
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, refine_landmarks=True)

    files = [f for f in os.listdir(faces_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    print(f"Extracting landmarks for {len(files)} images...")
    
    for filename in files:
        img_id = os.path.splitext(filename)[0]
        img_path = os.path.join(faces_dir, filename)
        img_bgr = cv2.imread(img_path)
        if img_bgr is None: continue
            
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        h, w, _ = img_rgb.shape
        results = face_mesh.process(img_rgb)
        if not results.multi_face_landmarks: continue
            
        face_landmarks = results.multi_face_landmarks[0]
        all_points = []
        grouped_points = {key: [] for key in LANDMARK_GROUPS.keys()}
        
        for idx, lm in enumerate(face_landmarks.landmark):
            px, py, pz = int(lm.x * w), int(lm.y * h), lm.z
            all_points.append({"id": idx, "x": px, "y": py, "z": pz})
            for group_name, indices in LANDMARK_GROUPS.items():
                if idx in indices:
                    grouped_points[group_name].append({"id": idx, "x": px, "y": py})

        landmark_data = {
            "image_id": img_id,
            "width": w,
            "height": h,
            "all_points": all_points,
            "groups": grouped_points
        }
        
        with open(os.path.join(landmarks_dir, f"{img_id}.json"), 'w', encoding='utf-8') as f:
            json.dump(landmark_data, f, indent=2)
            
    print(f"✅ Saved landmark JSON files in {landmarks_dir}")

if __name__ == '__main__':
    extract_landmarks('./processed/faces', './processed/landmarks')
