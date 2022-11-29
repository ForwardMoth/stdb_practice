# Проект по курсу "Специальные технологии баз данных и информационных систем"

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/ForwardMoth/stdb_practice/blob/postgres/README.en.md)

## Описание проекта: 

Создание c использованием языка python и библиотек базы данных и взаимодействия с ней. 
База данных содержит информацию о людях, группах, в которых находятся люди, а также список телефонов людей. 

- Для работы с проектом не забудьте отредактировать в файле config/config.yaml параметры ```user```, ```password```, ```db_name```, ```port```


## Проект реализован для 2 разных СУБД SQLite и PostgreSQL.

### Ветка master содержит вариант реализации на SQLite. Для перехода в неё: 

```git 
git checkout master
```
Здесь представлен неполный функционал: 

- Реализация 1:1 для таблиц группы и люди

### Ветка postgres содержит вариант реализации на PostgreSQL. Для перехода в неё:

```git 
git checkout postgres
```

Здесь представлен полный функционал: 

- Просмотр списка группы
- Просмотр списка групп для человека 
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

