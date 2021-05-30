# Parcial Final - Jair Duván Ayala Duarte
Crear una aplicación que permita procesar y visualizar el número tweets publicados por hashtags en
tiempo real. Los conteos tienen que realizarse en tiempo real utilizando spark-streaming en una
instancia de AWSEC2.

## Paso a paso

### Paso 1: Modificación del servidor
Se modifica el código visto en clase [https://github.com/camilousa/bigdata/tree/main/streaming-to-backend] de
server.py según nuestras necesidades

### Paso 2: Modificación del receptor de twitter
Se modifica el código visto en clase de la recepción de Tweets de ciertas palabras tweet.py

### Paso 3: Modificación del proceso
Se modifica el código visto en clase [https://github.com/camilousa/bigdata/tree/main/streaming-to-backend] de
process.py según nuestras necesidades

### Paso 4: Modificación de la página
Se modifica el código visto en clase [https://github.com/camilousa/bigdata/tree/main/streaming-to-backend] de
index.html según nuestras necesidades

### Paso 5: Se añade todo al EC2
Para este paso se enciende la máquina virtual y se agregan los archivos del paso 1-4 en este caso en la carpeta
parcial3

### Paso 6: Conexiones Putty
Se abren 3 conexiones con Putty las cuales tengan:

  Activar el entorno virtual
  ```
   source env/bin/activate
  ```
  Se debe ejecutar el archivo server.py
  ```
   python server.py
  ```
  Se debe ejecutar el archivo tweet.py
  ```
   python server.py
  ```
  Se debe ejecutar el archivo process.py
  ```
   spark-submit process.py localhost 9898
  ```

### Paso 7: Configurar Server - Instalar (Apache)

  Entramos como súper usuario
  ```
   sudo su
  ```
  
  Actualizamos todo
  ```
   apt-get update
   apt-get upgrade
  ```
  
  Salimos del modo súper usuario
  ```
   exit
  ```
  
  Instalamos Apache
  ```
   sudo apt-get install apache2
   Opcional: sudo apt-get install libapache2-mod-php
  ```
  
  Instalamos Apache
  ```
   sudo apt-get install apache2
   Opcional: sudo apt-get install libapache2-mod-php
  ```
  
### Paso 8: Configurar la página
  
  Nos dirigimos a la carpera de Apache
  ```
   cd /var/www/html
   
   otra opción:
   cd ..
   cd ..
   cd var/www/html
  ```
  
  Creamos nuestro HTML en la dirección actual
  ```
   sudo nano parcial3.html
  ```
Importante cambiar la dirección del EC2 en el parcial.html cada vez que se reinicie este
  
