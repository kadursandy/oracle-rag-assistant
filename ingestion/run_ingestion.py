
from ingestion.scraper import crawl
from ingestion.chunker import chunk_text
from ingestion.embedder import embed
from db.vector_store import insert_doc
from app.config import BASE_URL

data=crawl(BASE_URL)
for url,text in data:
    chunks=chunk_text(text)
    for c in chunks:
        insert_doc(c,url,embed(c))
print("Ingestion Complete")
