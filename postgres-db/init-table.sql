create schema demo
  create table testtable (id serial unique not null primary key, name varchar(50));

insert into demo.testtable (name) values ('ducth');