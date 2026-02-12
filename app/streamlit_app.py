
import streamlit as st,requests,uuid
st.title("Oracle RAG Assistant")
if "sid" not in st.session_state:
    st.session_state.sid=str(uuid.uuid4())
if "hist" not in st.session_state:
    st.session_state.hist=[]
msg=st.chat_input("Ask OCI...")
if msg:
    r=requests.post("http://api:8000/chat",params={"session_id":st.session_state.sid,"question":msg})
    ans=r.json()["answer"]
    st.session_state.hist.append(("user",msg))
    st.session_state.hist.append(("assistant",ans))
for role,text in st.session_state.hist:
    st.chat_message(role).write(text)
