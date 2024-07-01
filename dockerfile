FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y poppler-utils

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 3000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "3000"]


# docker build -t deepface-img2img .