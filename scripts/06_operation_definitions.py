import json
import os

OPERATION_TAXONOMY = {
    "rhinoplasty": {"arabic_name": "تجميل الأنف", "target_region": "nose"},
    "chin_augmentation": {"arabic_name": "تحديد وتكبير الذقن", "target_region": "chin"},
    "jawline_contouring": {"arabic_name": "تحديد الفك", "target_region": "jawline"},
    "facelift": {"arabic_name": "شد الوجه", "target_region": "lower_face"},
    "blepharoplasty": {"arabic_name": "تجميل الجفون والعيون", "target_region": "eyes"},
    "lip_enhancement": {"arabic_name": "تعديل وتكبير الشفاه", "target_region": "lips"}
}

def export_operations(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, 'operation_definitions.json'), 'w', encoding='utf-8') as f:
        json.dump(OPERATION_TAXONOMY, f, indent=2, ensure_ascii=False)
    print("✅ Phase 6 Complete! Exported 6 Surgical Operation Definitions.")

if __name__ == '__main__':
    export_operations('./docs')
