use flask-demo;
drop table if exists songs;
create table songs(id int NOT NULL AUTO_INCREMENT primary key,  title varchar(50), artist varchar(50), genre varchar(20));
insert into songs (title, artist, genre) values ("title 1", "title 1 artist", "title genre"), ("title 2", "title 2 artist", "title 2 genre"), ("title 3", "title 3 artist", "title 3 genre");