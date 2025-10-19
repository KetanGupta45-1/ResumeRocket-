from sentence_transformers import util
import torch

def compute_similarity(user_embs, target_embs, user_texts, target_texts):
    results = []
    for i, u_emb in enumerate(user_embs):
        scores = util.cos_sim(u_emb, target_embs)[0]
        best_score, best_idx = torch.max(scores, dim=0)
        results.append((user_texts[i], target_texts[int(best_idx.item())], float(best_score.item())))
    return results
