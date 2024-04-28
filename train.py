# Trainer for the deforestation detection model

import os
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import transforms
from torchvision.io import read_image
# Import deforestation model and dataset
from dataset import DeforestationDataset
from deforestation_model import DeforestObjectDectector

class DeforestationTrainer:
    """A class that trains a deforestation detection model."""
    
    def __init__(self, model_path, dataset_path):
        self.model = DeforestObjectDectector(model_path)
        self.dataset = DeforestationDataset(dataset_path)
        self.dataloader = DataLoader(self.dataset, batch_size=32, shuffle=True)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
    
    def train(self, num_epochs=10):
        """Train the deforestation detection model."""
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.Adam(self.model.parameters(), lr=0.001)
        
        for epoch in range(num_epochs):
            for images in self.dataloader:
                images = images.to(self.device)
                optimizer.zero_grad()
                outputs = self.model(images)
                loss = criterion(outputs, torch.zeros(images.size(0)).to(self.device))
                loss.backward()
                optimizer.step()
            
            print(f"Epoch {epoch+1}/{num_epochs}, Loss: {loss.item()}")
        
        print("Training complete.")
        
    def save_model(self, save_path):
        """Save the trained deforestation detection model."""
        torch.save(self.model.state_dict(), save_path)
    
    def predict(self, image_path):
        """Predict deforestation objects in the image."""
        image = read_image(image_path).to(self.device)
        return self.model(image)

def main():
    model_path = "deforestation_model.pth"
    dataset_path = "deforestation_dataset"
    trainer = DeforestationTrainer(model_path, dataset_path)
    trainer.train()
    trainer.save_model(model_path)
    prediction = trainer.predict("test_image.jpg")
    print(prediction)

if __name__ == "__main__":
    main()