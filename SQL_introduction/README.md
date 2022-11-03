# SQL - Introduction
-   [Databases](https://intranet.hbtn.io/concepts/864)

## Resources

**Read or watch**:

-   [What is Database & SQL?](https://intranet.hbtn.io/rltoken/jRAhwW4u4YvZtLtMGU2_6g "What is Database & SQL?")
-   [A Basic MySQL Tutorial](https://intranet.hbtn.io/rltoken/m_0RMf4RcC5NrHyjY1xN3w "A Basic MySQL Tutorial")
-   [Basic SQL statements: DDL and DML](https://intranet.hbtn.io/rltoken/-Qrnbp5eKmo7ajPDZekjfg "Basic SQL statements: DDL and DML")  (_no need to read the chapter “Privileges”_)
-   [Basic queries: SQL and RA](https://intranet.hbtn.io/rltoken/wXN5s1qexSTMh--NkTF1_w "Basic queries: SQL and RA")
-   [SQL technique: functions](https://intranet.hbtn.io/rltoken/7khGjnehvjHnqNZ9yizggg "SQL technique: functions")
-   [SQL technique: subqueries](https://intranet.hbtn.io/rltoken/xnJcopQTZyUke3LdAkOwow "SQL technique: subqueries")
-   [What makes the big difference between a backtick and an apostrophe?](https://intranet.hbtn.io/rltoken/QEr3XcBPhIR-E8NSSn1nzg "What makes the big difference between a backtick and an apostrophe?")
-   [MySQL Cheat Sheet](https://intranet.hbtn.io/rltoken/mNcGgvhZNG0dbFe23E-EjA "MySQL Cheat Sheet")
-   [MySQL 8.0 SQL Statement Syntax](https://intranet.hbtn.io/rltoken/ePNUeloWxfiXwec7HeKe7Q "MySQL 8.0 SQL Statement Syntax")


### General

-   What’s a database
-   What’s a relational database
-   What does SQL stand for
-   What’s MySQL
-   How to create a database in MySQL
-   What does  `DDL`  and  `DML`  stand for
-   How to  `CREATE`  or  `ALTER`  a table
-   How to  `SELECT`  data from a table
-   How to  `INSERT`,  `UPDATE`  or  `DELETE`  data
-   What are  `subqueries`
-   How to use MySQL functions

## Requirements

### General

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be executed on Ubuntu 20.04 LTS using  `MySQL 8.0`  (version 8.0.25)
-   All your files should end with a new line
-   All your SQL queries should have a comment just before (i.e. syntax above)
-   All your files should start by a comment describing the task
-   All SQL keywords should be in uppercase (`SELECT`,  `WHERE`…)
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   The length of your files will be tested using  `wc`

## More Info

### Comments for your SQL file:

```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$

```

### Install MySQL 8.0 on Ubuntu 20.04 LTS

```
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$

```

Connect to your MySQL server:

```
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$

```
