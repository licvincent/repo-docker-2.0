# Usa la imagen base
FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu20.04

# Establece el directorio de trabajo
WORKDIR /app

# Copia el contenido del proyecto
COPY . /app

# Instala Python y pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Actualiza pip
RUN python3 -m pip install --upgrade pip

# Instala las dependencias
RUN python3 -m pip install -r requirements.txt

# Especifica el comando para ejecutar la app
CMD ["python3", "app.py"]

