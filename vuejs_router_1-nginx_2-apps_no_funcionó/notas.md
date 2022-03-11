# Notas Vuejs+Nginx

## Observaciones

Posts para hacer funcionar varias apps en la misma URL
https://stackoverflow.com/a/51107960/6177246

Para hacer que la url sea `/localhost/app1/etc` hay que agregar en:

1) vue.config.js:

```js
module.exports = defineConfig({
  transpileDependencies: true,
  publicPath: '/app1/' // Agregar esto
})
```

2) router/index.js

```js
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  base: '/app1', // Agregar esto
  routes
})
```

3) nginx.conf


```nginx
location / {
    root /app;
    index index.html;
    try_files $uri $uri/ /index.html; # Hay que agregar un redirect 404 en vue router
}
location /app2 {
    root /app2;
    index index.html;
    try_files $uri $uri/ /index.html; # Hay que agregar un redirect 404 en vue router
}
```

## Para iniciar el contenedor:

```bash
docker build . -t vuejs-nginx-router-2-apps
```

```bash
docker run -d -p 80:80 vuejs-nginx-router-2-apps
```

Si muestra este error:

```
failed to solve with frontend dockerfile.v0: failed to read dockerfile: open /var/lib/docker/tmp/buildkit-mount847288160/Dockerfile: no such file or directory
```

Probar desactivando buildkit

[Ver este post](https://stackoverflow.com/a/66839653/6177246)