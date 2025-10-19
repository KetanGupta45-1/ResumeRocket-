from sentence_transformers import SentenceTransformer
import torch

def encode_texts(model_name, texts, batch_size, device):
    model = SentenceTransformer(model_name)
    all_embs = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]
        embs = model.encode(batch, convert_to_tensor=True, device=device)
        all_embs.append(embs)
    return torch.cat(all_embs, dim=0) if all_embs else torch.empty(0)
