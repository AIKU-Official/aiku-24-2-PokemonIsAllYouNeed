import torch
from PIL import Image
import open_clip

import os

import numpy as np
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
from tqdm import tqdm

device = 'cuda:0'

model, _, preprocess = open_clip.create_model_and_transforms('ViT-g-14', pretrained='laion2b_s34b_b88k')

def run_one_image(img, model):
    
    embedding = model.encode_image(img)
    
    return embedding

def extract_embedding(img, model=model):
    img = preprocess(img)
    img = img.unsqueeze(0)
    embedding = model.encode_image(img)
    
    return embedding

class CustomImageDataset(Dataset):
    def __init__(self, image_list, image_name_list, preprocess):
        self.image_list = image_list
        self.image_name_list = image_name_list

    def __len__(self):
        return len(self.image_list)

    def __getitem__(self, idx):
        img = self.image_list[idx]
        img = preprocess(img)
        
        return self.image_name_list[idx], img