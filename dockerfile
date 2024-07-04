FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir fastapi \
    uvicorn \

COPY . .

RUN cd model && python download_models.py && cd ..
RUN cd src/CodeFormer/CodeFormer/weights && python download_weights.py && cd ../../../../

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

# docker build -t deepfacehuman-img2img .