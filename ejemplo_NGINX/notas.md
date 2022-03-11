
### Construir imagen a partir de dockerfile

docker build -t static-nginx .

### Iniciar contenedor

#### Ejemplo básico 1

docker run --rm -it -p 8080:80 --name prueba-nginx static-nginx

[ver](http://localhost:8080)

--rm hace que una vez que el al momento de cerrar el proceso se pare el contenedor
--it permite ver la consola del nginx

#### Ejemplo básico 2

docker run -it --rm -d -p 8080:80 --name prueba-nginx static-nginx



#### Con mounts

Los mounts sincronizan el directorio en la pc con el contenedor

docker run --name mynginx2 --mount type=bind,source=/www,target=/usr/share/nginx/html,readonly --mount source=/var/nginx/conf,target=/etc/nginx/conf,readonly -p 80:80 -d nginx