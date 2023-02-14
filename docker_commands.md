## Работа с образами
`docker images` или `docker image ls` — посмотреть список образов ([ссылка](https://docs.docker.com/engine/reference/commandline/images/), [ссылка](https://docs.docker.com/engine/reference/commandline/image_ls/))

`docker rmi <образ> [образ...]` или `docker image rm <образ> [образ...]` — удалить образ(ы) ([ссылка](https://docs.docker.com/engine/reference/commandline/rmi/), [ссылка](https://docs.docker.com/engine/reference/commandline/image_rm/))

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

`docker exec <контейнер> команда` — запустить команду в работающем контейнер ([ссылка](https://docs.docker.com/engine/reference/commandline/exec/))

- `docker exec -it <контейнер> bash` — запустить bash процесс и «войти» в контейнер ([ссылка](https://docs.docker.com/engine/reference/commandline/exec/#run-docker-exec-on-a-running-container))

## Инструкции Dockerfile'а

`FROM` — задаем базовый образ, на основе которого собираем новый ([ссылка](https://docs.docker.com/engine/reference/builder/#from))

`COPY` — копируем файл с нашей файловой системы в файловую систему контейнеров ([ссылка](https://docs.docker.com/engine/reference/builder/#copy))

`ADD` — добавляем файл или ссылку с нашей файловой системы в образ ([ссылка](https://docs.docker.com/engine/reference/builder/#add))

`RUN` — выполняем команду ([ссылка](https://docs.docker.com/engine/reference/builder/#run))

`WORKDIR` — устанавливаем рабочую директорию ([ссылка](https://docs.docker.com/engine/reference/builder/#workdir))

`ENTRYPOINT` — задаем точку входа для запуска контейнера ([ссылка](https://docs.docker.com/engine/reference/builder/#entrypoint))

`CMD` — задаем точку входа для запуска контейнера ([ссылка](https://docs.docker.com/engine/reference/builder/#cmd))

Со списком инструкций можно ознакомиться в документации ([ссылка](https://docs.docker.com/engine/reference/builder/)).
