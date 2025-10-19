from sentence_transformers import SentenceTransformer
from Matching.build_embeddings import build_embeddings
from Matching.compute_similarity import compute_similarity

def semantic_skill_matcher(user_skill_texts, target_skill_texts, model_name, cache_path, batch_size):
    """
    Returns: list of tuples (user_skill, matched_target_skill, similarity_score)
    """
    model = SentenceTransformer(model_name)
    device = model.device
    targets, target_embs = build_embeddings(target_skill_texts, model_name, cache_path, batch_size, device)
    user_embs = model.encode(user_skill_texts, convert_to_tensor=True, device=device)
    return compute_similarity(user_embs, target_embs, user_skill_texts, targets)
