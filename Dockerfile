
FROM python:3.11
WORKDIR /app
ENV PYTHONPATH=/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8501 8000
CMD ["sh","-c","uvicorn api.server:app --host 0.0.0.0 --port 8000 & streamlit run app/streamlit_app.py --server.address 0.0.0.0 --server.port 8501"]
