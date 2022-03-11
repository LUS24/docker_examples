# Docker

## [Seguridad](https://github.com/BretFisher/ama/issues/17#issuecomment-400163774)

## WSL2


Achivo de configuración: `C:\Users\leo24\.wslconfig` (no lo estoy usando)

Solución para limitar el [uso excesivo de memoria](https://github.com/microsoft/WSL/issues/4166):

```
[wsl2]
memory=6GB
swap=0
localhostForwarding=true
```

Localización default de los volumenes de Docker:

`C:\Users\username\AppData\Local\Docker\wsl\data\ext4.vhdx`

La localización de la distribución de docker está en:

`C:\Users\username\AppData\Local\Docker\wsl\distro\ext4.vhdx`

## [Cambiar de lugar el archivo .vhdx](https://github.com/microsoft/WSL/issues/4699#issuecomment-660104214)

[Ejemplo](https://github.com/MicrosoftDocs/WSL/issues/412#issuecomment-501913246)

Recordar poner default version 2 en caso de ser necesario
`wsl --set-default-version 2`

```bash
wsl --shutdown
wsl -l -v
wsl --export <DistroName> <PathToTarArchive>
wsl --unregister <DistroName>
wsl --import <DistroName> <PathToDistroNewDirectory> <PathToTarArchive>
wsl -l -v
```

cd D:\WSL\Docker

wsl --shutdown
wsl -l -v
wsl --export docker-desktop-data ./docker-desktop-data.tar
wsl --unregister docker-desktop-data
wsl --import docker-desktop-data . ./docker-desktop-data.tar
wsl -l -v


## Acceso a través de la red a los mounts de docker

```
\\wsl$\docker-desktop
\\wsl$\docker-desktop-data
```

## Conectarse a un contenedor

docker exec -it prueba-nginx /bin/bash