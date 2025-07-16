from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

documents = [
    "PwC focuses on GenAI strategy and responsible AI.",
    "Prompt engineering improves LLM performance.",
    "Vector databases store document embeddings.",
    "OpenAI GPT models can answer business questions."
]

model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(documents)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

def retrieve_docs(query, k=2):
    query_vector = model.encode([query])
    D, I = index.search(query_vector, k)
    return [documents[i] for i in I[0]]
