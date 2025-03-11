
# Usa una imagen base de Python

FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de la aplicación
COPY . /app

# Instala las dependencias
RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt


# Expone el puerto en el que la aplicación escuchará
EXPOSE 8080

# Comando para ejecutar la aplicación
CMD ["python", "app.py"] # Reemplaza app.py con el nombre de tu script
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:server"]
