create table cars (ID int(5),
vin varchar(45),
manufacturer varchar(45) ,
model varchar(45),
year int(5),
color varchar(15),
cidinvoice int(15),
Foreign Key(cidinvoice) references invoices(ID),
PRIMARY KEY(ID)
);


create table customers (
ID int(5),
customerID int(10),
name varchar(45),
phone int(20),
email varchar(45),
address varchar(45),
city varchar(45),
state varchar(45),
country varchar(45),
zip int(5),
PRIMARY KEY(ID)
);


create table salespersons (
ID int(5),
staffID int(45),
name varchar(45),
store varchar(45),
PRIMARY KEY(ID)
);

create table invoices (
ID int(5),
invoiceID int(15),
date DATE,
car int(15),
idcustomer int(15),
idstaff int(15),
Foreign Key(idcustomer) references customers(ID),
Foreign Key(idstaff) references salespersons(ID),
PRIMARY KEY(ID))
;

INSERT INTO cars (vin, manufacturer, model, year, color,cidinvoice)
VALUES ('3K096I98581DHSNUP', 'Volkswagen', 'Tiguan', 2019, 'Blue', 0),
("ZM8G7BEUQZ97IH46V","Peugeot" ,	"Rifter",	2019 ,	"Red",1),
("RKXVNNIHLVVZOUB4M", "Ford", 	"Fusion" 	,2018 ,	"White",2),
("HKNDGS7CU31E9Z7JW" ,"Toyota" ,	"RAV4" ,2018 ,	"Silver",3),
("DAM41UDN3CHU2WVF6" ,"Volvo" ,	"V60" 	,2019 ,	"Gray",4),
("DAM41UDN3CHU2WVF6", "Volvo" ,"V60 Cross Country" ,2019 ,"Gray",5);


INSERT INTO customers (customerID, name, phone, email, address, city, state, country, zipcode)
VALUES ("10001", "Pablo Picasso", 346361763, "d@w.com", "Paseo de la Chopera, 14", "Madrid", 'Madrid', 'Spain', 28045);

INSERT INTO salespersons(staffID, name, store)
VALUES ("00001", "Petey Cruiser", "Madrid");

INSERT INTO invoices(invoiceID, date, idcar, idcustomer, idstaff)
VALUES ("852399038", '2018-01-01', 1, 1, 1);