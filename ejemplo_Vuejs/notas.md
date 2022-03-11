# Notas Vuejs+Nginx

## Para iniciar el contenedor:

```bash
docker build . -t vuejs-nginx
```

```bash
docker run -d -p 80:80 vuejs-nginx
curl localhost:8080
```


Si muestra este error:

```
failed to solve with frontend dockerfile.v0: failed to read dockerfile: open /var/lib/docker/tmp/buildkit-mount847288160/Dockerfile: no such file or directory
```

Probar desactivando buildkit

[Ver este post](https://stackoverflow.com/a/66839653/6177246)