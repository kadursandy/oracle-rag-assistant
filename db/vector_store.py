
import psycopg2,time
from app.config import DB_CONFIG

for _ in range(10):
    try:
        conn=psycopg2.connect(**DB_CONFIG)
        break
    except:
        time.sleep(2)
cur=conn.cursor()
cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
cur.execute("CREATE TABLE IF NOT EXISTS documents(id SERIAL PRIMARY KEY,content TEXT,url TEXT,embedding VECTOR(1536));")
conn.commit()


def insert_doc(content,url,emb):
    cur.execute("INSERT INTO documents(content,url,embedding) VALUES(%s,%s,%s)",(content,url,emb))
    conn.commit()


def search(qemb, k=5):
    try:
        cur.execute(
            "SELECT content,url FROM documents ORDER BY embedding <-> %s LIMIT %s",
            (qemb, k)
        )
        return cur.fetchall()
    except Exception as e:
        conn.rollback()
        print("Search error:", e)
        return []
