import torch

def save_embeddings(cache_path, targets, embeddings):
    try:
        torch.save({'targets': targets, 'embeddings': embeddings.cpu()}, cache_path)
    except Exception:
        pass