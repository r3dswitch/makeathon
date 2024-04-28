import os
import torch

from torchvision.io import read_image
from torchvision.ops.boxes import masks_to_boxes
from torchvision import tv_tensors
from torchvision.transforms.v2 import functional as F

class DeforestationDataset(torch.utils.data.Dataset):
    """A class that loads a dataset of deforestation images."""
    
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.images = os.listdir(root_dir)
    
    def __len__(self):
        return len(self.images)
    
    def __getitem__(self, idx):
        img_path = os.path.join(self.root_dir, self.images[idx])
        image = read_image(img_path)
        if self.transform:
            image = self.transform(image)
        return image