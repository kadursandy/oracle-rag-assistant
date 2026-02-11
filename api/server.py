
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from openai import OpenAI
from app.chat_memory import load_history,save_message
from app.agent import answer

client=OpenAI()
app=FastAPI()

@app.post("/chat")
def chat(session_id:str,question:str):
    hist=load_history(session_id)
    ans=answer(question,hist)
    save_message(session_id,"user",question)
    save_message(session_id,"assistant",ans)
    return {"answer":ans}

@app.post("/chat-stream")
def chat_stream(session_id:str,question:str):
    hist=load_history(session_id)
    msgs=hist+[{"role":"user","content":question}]
    def gen():
        full=""
        stream=client.chat.completions.create(model="gpt-4o-mini",messages=msgs,stream=True)
        for c in stream:
            d=c.choices[0].delta.content
            if d:
                full+=d
                yield d
        save_message(session_id,"user",question)
        save_message(session_id,"assistant",full)
    return StreamingResponse(gen(),media_type="text/plain")
