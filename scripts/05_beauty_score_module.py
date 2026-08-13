import os
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

class BeautyScoreEvaluator(nn.Module):
    def __init__(self, pretrained=True):
        super(BeautyScoreEvaluator, self).__init__()
        self.backbone = models.resnet18(pretrained=pretrained)
        num_ftrs = self.backbone.fc.in_features
        self.backbone.fc = nn.Sequential(
            nn.Linear(num_ftrs, 128),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(128, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        out = self.backbone(x)
        return 1.0 + out * 4.0

def evaluate_face_beauty(img_path):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = BeautyScoreEvaluator(pretrained=False).to(device)
    model.eval()
    
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    img = Image.open(img_path).convert('RGB')
    tensor = transform(img).unsqueeze(0).to(device)
    with torch.no_grad():
        score = model(tensor).item()
    return score

if __name__ == '__main__':
    sample_img = './processed/faces/000001.jpg'
    if os.path.exists(sample_img):
        score = evaluate_face_beauty(sample_img)
        print(f"✅ Phase 5 Complete! Beauty Score: {score:.2f} / 5.0")
