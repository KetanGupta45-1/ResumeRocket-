from Matching.embed_text import encode_texts
from Matching.save_embedding import save_embeddings
from Matching.load_embedding import load_embeddings

def build_embeddings(targets, model_name, cache_path, batch_size, device):
    """
    Build (or load) embeddings for targets. Uses cache only if cached targets exactly match
    the requested targets list.

    Returns: (targets_list, embeddings_tensor_on_device)
    """

    loaded_targets, loaded_embs = load_embeddings(cache_path, device)
    if loaded_embs is not None and loaded_targets == targets:
        return loaded_targets, loaded_embs

    targets_unique = list(dict.fromkeys(targets))
    embeddings = encode_texts(model_name, targets_unique, batch_size, device)
    save_embeddings(cache_path, targets_unique, embeddings)
    return targets_unique, embeddings.to(device)
