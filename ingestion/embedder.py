
from langchain_openai import OpenAIEmbeddings
emb=OpenAIEmbeddings(model="text-embedding-3-small")
def embed(text):
    return emb.embed_query(text)
