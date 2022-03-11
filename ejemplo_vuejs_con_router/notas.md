# Notas Vuejs+Nginx

## Observaciones

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

nginx.conf
```
location /app1 {
    root   /app;
    index  index.html;
    try_files $uri $uri/ /index.html;
}
```

## Para iniciar el contenedor:

```bash
docker build . -t vuejs-nginx-router
```

```bash
docker run -d -p 80:80 vuejs-nginx-router
```

Si muestra este error:

```
failed to solve with frontend dockerfile.v0: failed to read dockerfile: open /var/lib/docker/tmp/buildkit-mount847288160/Dockerfile: no such file or directory
```

Probar desactivando buildkit

[Ver este post](https://stackoverflow.com/a/66839653/6177246)