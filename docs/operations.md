# Operation Taxonomy — Cosmetic Surgery AI

## 1. Rhinoplasty (تجميل الأنف)
- Target region: nose (bridge, tip, nostrils)
- Description: reshape nose bridge/tip proportions
- Limits: no change to eyes, cheeks, or jaw
- Evaluation: nose region SSIM/LPIPS + identity similarity elsewhere

## 2. Chin Augmentation (تجميل الذقن)
- Target region: chin/jaw lower point
- Description: adjust chin projection/shape
- Limits: no change to nose, lips, or upper face
- Evaluation: chin contour comparison + identity similarity

## 3. Jawline Contouring (نحت خط الفك)
- Target region: jawline (left/right mandible edge)
- Description: sharpen/adjust jaw contour
- Limits: no change to eyes, nose, mouth
- Evaluation: jaw contour metrics + identity similarity

## 4. Facelift (شد الوجه)
- Target region: cheeks + lower face skin
- Description: reduce sagging, tighten skin appearance
- Limits: no change to bone structure landmarks
- Evaluation: skin texture/smoothness score + identity similarity

## 5. Blepharoplasty (تجميل الجفون)
- Target region: upper/lower eyelids
- Description: adjust eyelid skin/shape
- Limits: no change to eyebrows, nose, or eye color/shape
- Evaluation: eyelid region fidelity + identity similarity

## 6. Lip Enhancement (تكبير الشفايف)
- Target region: lips (upper + lower)
- Description: adjust lip volume/shape
- Limits: no change to nose, chin, or teeth visibility
- Evaluation: lip region fidelity + identity similarity
