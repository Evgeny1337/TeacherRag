from sentence_transformers import SentenceTransformer

_MODEL_NAME = "BAAI/bge-small-en-v1.5"
_model: SentenceTransformer | None = None


def get_embedder() -> SentenceTransformer:
    global _model
    model = _model
    if model is None:
        model = SentenceTransformer(_MODEL_NAME)
        _model = model
    return model


def embed_text(text: str) -> list[float]:
    return get_embedder().encode(text).tolist()
