create database projeto_evidencia;
use projeto_evidencia;
create table funcionarios ( 
	id int not null primary key auto_increment,
    nome varchar(255),
    descricao varchar(255),
    cargo varchar(150),
    empresa varchar(200),
    email varchar(255),
    github varchar(100),
    linkedin varchar(150),
    telefone varchar(11),
    curriculo varchar(80),
    foto varchar(80) );

select*from funcionarios;



