use database_hood_mjc-15-a;
drop table if exists order_items;
drop table if exists menu_items;
drop table if exists any_order;
drop table if exists reservation;
drop table if exists customers;

create table customers (
    -- no values are UNIQUE, because one person may open multiple accounts 
    -- (e.g. for a separate corporate account).
    customerID int not null auto_increment primary key,
    name varchar(20) not null,
    email varchar(20),
    PhoneNumber varchar(11) not null,
    address varchar(50),
    dob date DEFAULT '2100-01-01',  -- minors should not be served alcohol.
    card int(4),
    membership boolean DEFAULT false
);

create table reservation (
    reservationID int not null auto_increment primary key,
    customerID int,
    reservationDateTime datetime,
    size int,
    tableNumber int,
    specialRequests varchar(100),

    foreign key(customerID) references customers(customerID)
    -- default settings for reacting to changes.
);

create table any_order (
    orderID int not null auto_increment primary key,
    reservationID int,
    customerID int,
    totalBill decimal(10,2),
    server varchar(20),

    foreign key(reservationID) references reservation(reservationID),
    foreign key(customerID) references customers(customerID),
    -- default settings for reacting to changes.

    check (reservationID is not null or customerID is not null),
    check (reservationID is null or customerID is null)
    -- these constraints ensure that each order is associated with
    -- either a reservation or a customer, and not (directly) with both.
);

create table menu_items (
    itemID int not null auto_increment primary key,
    itemName varchar(20) UNIQUE,
    description varchar(50),
    price decimal(10,2),
    category varchar(20)
);

create table order_items (
    orderID int,
    itemID int,
    primary key(orderID, itemID),
    foreign key(orderID) references any_order(orderID),
    foreign key(itemID) references menu_items(itemID)
    -- default settings for reacting to changes.
);

