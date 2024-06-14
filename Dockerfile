# Utilizar una imagen base oficial de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar las dependencias del sistema
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsndfile1

# Copiar el archivo de requerimientos e instalarlos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código del proyecto
COPY . .

# Exponer el puerto que usa Django (8000 por defecto)
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
