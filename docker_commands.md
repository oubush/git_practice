## Работа с образами
`docker images` или `docker image ls` — посмотреть список образов ([ссылка](https://docs.docker.com/engine/reference/commandline/images/), [ссылка](https://docs.docker.com/engine/reference/commandline/image_ls/))

`docker rmi <образ> [образ...]` или `docker image rm <образ> [образ...]` — удалить образ(ы) ([ссылка](https://docs.docker.com/engine/reference/commandline/rmi/), [ссылка](https://docs.docker.com/engine/reference/commandline/image_rm/))

`docker pull <образ>:<тэг>`

## Работа с контейнерами

`docker run <образ>` — поднять контейнер на основе образа ([ссылка](https://docs.docker.com/engine/reference/commandline/run/))

- `docker run --name <имя> <образ>` — при поднятии присвоить имя контейнеру ([ссылка](https://docs.docker.com/engine/reference/run/#name---name))

- `docker run --rm <образ>` — удалять контейнер после завершения его работы ([ссылка](https://docs.docker.com/engine/reference/run/#clean-up---rm))

- `docker run -it <образ>` — позволяет «войти» в контейнер во время его создания ([ссылка](https://docs.docker.com/engine/reference/commandline/run/#assign-name-and-allocate-pseudo-tty---name--it), [ссылка](https://docs.docker.com/engine/reference/run/#foreground))

- `docker run -d <образ>` — поднять контейнер в фоновом режиме ([ссылка](https://docs.docker.com/engine/reference/run/#detached--d))

`docker ps` — список активных (работающих) контейнеров ([ссылка](https://docs.docker.com/engine/reference/commandline/ps/))

- `docker ps -a` — список всех контейнеров ([ссылка](https://docs.docker.com/engine/reference/commandline/ps/#show-both-running-and-stopped-containers))

`docker stop <контейнер> [контейнер...]` — остановить работающий(ие) контейнер(ы) ([ссылка](https://docs.docker.com/engine/reference/commandline/stop/))

`docker start <контейнер> [контейнер...]` — запустить остановленный(ые) контейнер(ы) ([ссылка](https://docs.docker.com/engine/reference/commandline/start/))

`docker rm <контейнер> [контейнер...]` — удалить контейнер(ы) ([ссылка](https://docs.docker.com/engine/reference/commandline/rm/))

`docker exec <контейнер> команда` — запустить команду в работающем контейнере ([ссылка](https://docs.docker.com/engine/reference/commandline/exec/))

- `docker exec -it <контейнер> bash` — запустить bash процесс и «войти» в контейнер ([ссылка](https://docs.docker.com/engine/reference/commandline/exec/#run-docker-exec-on-a-running-container))

`docker system df`

## Инструкции Dockerfile'а

`FROM` — задаем базовый образ, на основе которого собираем новый ([ссылка](https://docs.docker.com/engine/reference/builder/#from))

`COPY` — копируем файл с нашей файловой системы в файловую систему контейнеров ([ссылка](https://docs.docker.com/engine/reference/builder/#copy))

`ADD` — добавляем файл или ссылку с нашей файловой системы в образ ([ссылка](https://docs.docker.com/engine/reference/builder/#add))

`RUN` — выполняем команду ([ссылка](https://docs.docker.com/engine/reference/builder/#run))

`WORKDIR` — устанавливаем рабочую директорию ([ссылка](https://docs.docker.com/engine/reference/builder/#workdir))

`ENTRYPOINT` — задаем точку входа для запуска контейнера ([ссылка](https://docs.docker.com/engine/reference/builder/#entrypoint))

`CMD` — задаем точку входа для запуска контейнера ([ссылка](https://docs.docker.com/engine/reference/builder/#cmd))

Со списком инструкций можно ознакомиться в документации ([ссылка](https://docs.docker.com/engine/reference/builder/)).

`docker build -t <новое_имя_образа> <директория_с_контекстом>`

`docker commit <контейнер> <новое_имя_образа>:<тэг>`

## Синхронизация файлов

`docker cp <путь на хосте> <название контейнера>:<путь в контейнере>` - скопировать файл или папку с хоста в контейнер  
`docker cp <название контейнера>:<путь в контейнере> <путь на хосте>` - скопировать файл или папку с контейнера на хост

Ссылки:  
[Volume](https://docs.docker.com/storage/volumes/)  
[Bind mount](https://docs.docker.com/storage/bind-mounts/)

`docker volume ls` — вывести список вольюмов ([ссылка](https://docs.docker.com/engine/reference/commandline/volume_ls/))

`docker volume create <название>` — создать вольюм ([ссылка](https://docs.docker.com/engine/reference/commandline/volume_create/))

`docker volume rm <название>` — удалить вольюм ([ссылка](https://docs.docker.com/engine/reference/commandline/volume_rm/))

`docker volume prune` — удалить вольюмы, которые не используются контейнерами ([ссылка](https://docs.docker.com/engine/reference/commandline/volume_prune/))

`docker volume inspect <название>`

### Bind mount:
`docker run -v <полный_путь_на_хосте>:<полный_путь_в_контейнере> <образ>`

### Volume:
`docker run -v <название_вольюма>:<полный_путь_в_контейнере> <образ>`

### Readonly режим
`docker run -v <полный_путь_на_хосте>:<полный_путь_в_контейнере>:ro <образ>`

## Переменные окружения

`ENV` — инструкция в Dockerfile, которая позволяет задавать переменные окружения в контейнерах ([ссылка](https://docs.docker.com/engine/reference/builder/#env)).

      * Не задавайте через эту инструкцию секретные данные

`docker run -e <НАЗВАНИЕ_ПЕРЕМЕННОЙ>=<значение> <образ>` — позволяет задать переменную окружения в конкретном контейнере ([ссылка](https://docs.docker.com/engine/reference/commandline/run/#set-environment-variables--e---env---env-file)).

`docker run --env-file <НАЗВАНИЕ_ФАЙЛА_С_ПЕРЕМЕННЫМИ> <образ>` — позволяет задать переменные окружения в конкретном контейнере из файла ([ссылка](https://docs.docker.com/engine/reference/commandline/run/#set-environment-variables--e---env---env-file)).

## Логи

`docker logs <контейнер>` — позволяет вытащить логи из контейнера ([ссылка](https://docs.docker.com/engine/reference/commandline/logs/))

- `docker logs -f <контейнер>` — не отключаемся от контейнера

- `docker logs -t <контейнер>` — добавляем время к логам

Ссылка: [View container logs](https://docs.docker.com/config/containers/logging/).

## Порты

`EXPOSE` — инструкция в Dockerfile, которая позволяет сообщить пользователю, какой(ие) порт(ы) слушает приложение внутри контейнера. Не прокидывает порты на хост ([ссылка](https://docs.docker.com/engine/reference/builder/#expose))

`docker run -p <порт_на_хосте>:<порт_в_контейнере> <образ>` — связывает порт внутри контейнера с портом на хосте ([ссылка](https://docs.docker.com/engine/reference/commandline/run/#publish-or-expose-port--p---expose)).

`docker run -p <IP_адрес_на_хосте>:<порт_на_хосте>:<порт_в_контейнере> <образ>` — по умолчанию адрес на хосте задается 0.0.0.0. При поднятии можно изменить этот адрес. Например: `docker run -p 127.0.0.1:80:80 nginx`

## Сети

`docker network ls` — список сетей ([ссылка](https://docs.docker.com/engine/reference/commandline/network_ls/))

`docker network create <название_сети>` — создать сеть ([ссылка](https://docs.docker.com/engine/reference/commandline/network_create/))

`docker network rm <название_сети>` — удалить сеть ([ссылка](https://docs.docker.com/engine/reference/commandline/network_rm/))

`docker run --net=<название_сети> <образ>` — подключаем контейнер к сети ([ссылка](https://docs.docker.com/engine/reference/commandline/run/#connect-a-container-to-a-network---network), [ссылка](https://docs.docker.com/engine/reference/run/#network-settings))

`docker inspect <название_или_ID_объекта>` — получить информацию об объектах докера (контейнер, образ, вольюм, сеть) ([ссылка](https://docs.docker.com/engine/reference/commandline/inspect/))

`docker network connect <название_сети> <название_контейнера>` - подключение контейнера к сети

Ссылка: [Networking overview](https://docs.docker.com/network/)
