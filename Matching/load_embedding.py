import os
import torch

def load_embeddings(cache_path, device):
    if os.path.exists(cache_path):
        try:
            data = torch.load(cache_path)
            return data['targets'], data['embeddings'].to(device)
        except Exception:
            return None, None
    return None, None
