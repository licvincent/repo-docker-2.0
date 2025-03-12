FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu20.04

# Instalar pip
RUN apt-get update && apt-get install -y python3-pip

WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:server"]
