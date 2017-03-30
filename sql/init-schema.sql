drop database IF EXISTS `mock-FlaskSqlAlchemy`;
create database `mock-FlaskSqlAlchemy`;

use `mock-FlaskSqlAlchemy`;

drop table IF EXISTS some_table;
create table some_table (
  id int AUTO_INCREMENT,
  name text,
  PRIMARY KEY(id)
);

insert into some_table(name) values
  ('some name 01'),
  ('some name 02')
;
