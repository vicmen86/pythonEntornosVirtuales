#se crea un contenedor
FROM python:3.10 
#creamos una carpeta dentro de ese contenedor
WORKDIR /app
#copiamos las especificaiones del archivo requirements.txt a un archivo nuevo del contenedor
COPY requirements.txt /app/requirements.txt
#instalamos todos los requerimientbos, evitamos el cache y si hay actualizaciones del gestor de apquetes se actualice
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
# El punto especifica todo lo que contiene la carpeta actual 
COPY . /app
#necesitamos que el contenedor este en una ejecucion continua, se usa lenguaje bach para dar esa instruccion
CMD bash -c "while true; do sleep 1; done"