# Project on the course "Special technologies of databases and information systems"

[![ru](https://img.shields.io/badge/lang-ru-red.svg)](https://github.com/ForwardMoth/stdb_practice/tree/postgres)

## Project description: 

Creating a database and actions with it using Python and modules SQLite3 and SQLalchemy.
The database contains information about people, groups, in which people are studied and also a list of people's phone numbers.

- To work with a project don't forget to edit in file config/config.yaml parametrs of database user and database connection ```user```, ```password```, ```db_name```, ```port```

## The project implemented for 2 different DBMS SQLite and PostgreSQL.

### The branch [master](https://github.com/ForwardMoth/stdb_practice/tree/master) contains an realisation on DBMS SQLite. To switch in terminal: 

```git 
git checkout master
```

There is not all functionality is presented here: 

- A 1:1 ratio is implemented for the groups and people tables

### The branch postgres contains an realisation on DBMS PostgreSQL. To switch in terminal: 

```git 
git checkout postgres
```

There is all functionality is presented here:

- Viewing the group list (all people in the group)
- Viewing a list of groups for a person (all groups for a person)
- Implementation of the M:M relationship for the groups and people tables

## Also operations are supported here:

### For people:

- Adding
- View
- Editing information
- Removal
- Search by last name

### For phones:

- Adding
- View by person
- Editing
- Removal

### For groups:

- Adding
- View
- Editing information
- Removal

### Important! Configuring DBMS postgresql. Linux or Windows

- Download and install [PostgreSQL](https://www.postgresql.org/download/)

- Go to the psql console

  - Windows:

    1. Adding the Windows environment variable the path to the bin folder in your installed version of Postgres:
    (my: C:\Program Files\PostgreSQL\14\bin)
    2. Go to the console and write: 
    ```cmd 
    psql -U postgres 
    ```

  - Linux: 
    ```bash 
    sudo -u postgres psql 
    ```

- Сreating user and setting password: 

```cmd 
CREATE ROLE "user" WITH LOGIN PASSWORD '1111';
```

- Create database and link it with your user 

```cmd 
create database testdb;
```

```cmd 
grant all privileges on database testdb to "user";
```
