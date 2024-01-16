create database ActD2;

create table sistema(
id int identity(1,1),
objetos varchar(250),
tarjetas varchar(16),
fechaex date,
intentos int,
fondos int,
pagos int
)

select * from sistema