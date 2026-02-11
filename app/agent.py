
from openai import OpenAI
from ingestion.embedder import embed
from db.vector_store import search

client=OpenAI()

def answer(question,history):
    qemb=embed(question)
    docs=search(qemb)
    context="\n\n".join([d[0] for d in docs])
    msgs=history+[{"role":"user","content":f"Context:\n{context}\nQuestion:{question}"}]
    res=client.chat.completions.create(model="gpt-4o-mini",messages=msgs)
    return res.choices[0].message.content
