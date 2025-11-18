FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y build-essential wget git libsndfile1 && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Create models dir and expose port for Streamlit if used
VOLUME /app/models
EXPOSE 8501

ENTRYPOINT ["python", "main.py"]
