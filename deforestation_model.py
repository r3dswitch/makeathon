# Pytorch
import torch
from torchvision import models
from torchvision import transforms
from PIL import Image
import numpy as np

class DeforestObjectDectector(torch.nn.Module):
    """A class that detects deforestation objects in satellite images."""

    def __init__(self, model_path):
        self.model = load_model(model_path)

    def predict(self, image):
        """Predict deforestation objects in the image."""
        return self.model.predict(image)
    
    def forward(self, x):
        return self.model(x)