
import psycopg2,time
from app.config import DB_CONFIG

for _ in range(10):
    try:
        conn=psycopg2.connect(**DB_CONFIG)
        break
    except:
        time.sleep(2)
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS chat_history(session_id TEXT,role TEXT,content TEXT);")
conn.commit()

def load_history(sid):
    cur.execute("SELECT role,content FROM chat_history WHERE session_id=%s",(sid,))
    return [{"role":r[0],"content":r[1]} for r in cur.fetchall()]

def save_message(sid,role,content):
    cur.execute("INSERT INTO chat_history VALUES(%s,%s,%s)",(sid,role,content))
    conn.commit()
