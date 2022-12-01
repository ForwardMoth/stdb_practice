# Проект по курсу "Специальные технологии баз данных и информационных систем"

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/ForwardMoth/stdb_practice/blob/postgres/README.en.md)

## Описание проекта: 

Создание базы данных c использованием языка python и библиотек (SQLlite3, SQLalchemy)  и взаимодействия с ней. 
База данных содержит информацию о людях, группах, в которых находятся люди, а также список телефонов людей. 

- Для работы с проектом не забудьте отредактировать в файле config/config.yaml параметры пользователя базы данных и подключение к базе данных ```user```, ```password```, ```db_name```, ```port```

## Проект реализован для 2 разных СУБД SQLite и PostgreSQL.

### Ветка [master](https://github.com/ForwardMoth/stdb_practice/tree/master) содержит вариант реализации на СУБД SQLite. Для перехода в неё в консоли: 

```git 
git checkout master
```
Здесь представлен неполный функционал: 

- Для таблиц группы и люди реализовано отношение 1:1

### Ветка postgres содержит вариант реализации на PostgreSQL. Для перехода в неё:

```git 
git checkout postgres
```

Здесь представлен полный функционал: 

- Просмотр списка группы (все люди в группе)
- Просмотр списка групп для человека  (все группы для 1 человека) 
- Реализация отношения M:M для таблиц группы и люди

### Важно! Настройка СУБД postgres. Linux или Windows.

- Скачиваем и устанавливаем [PostgreSQL](https://www.postgresql.org/download/)

- Заходим в консоль psql 

  - Для Windows:

    1. Добавляем переменную среды окружения Windows путь к папке bin в вашей установленной версии Postgres: 
    (у меня: C:\Program Files\PostgreSQL\14\bin)
    2. Заходим в консоль и пишем: 
    ```cmd 
    psql -U postgres 
    ```

  - Для Linux: 
    ```bash 
    sudo -u postgres psql 
    ```

- Создаём пользователя и задаем пароль: 

```cmd 
CREATE ROLE "user" WITH LOGIN PASSWORD '1111';
```

- Создаём базу данных и связываем её с пользователем 

```cmd 
create database testdb;
```

```cmd 
grant all privileges on database testdb to "user";
```

