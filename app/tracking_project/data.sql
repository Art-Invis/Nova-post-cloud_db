-- 1. Створення схеми та вибір бази даних
CREATE SCHEMA IF NOT EXISTS Tracking_sql;
USE Tracking_sql;

-- 2. Видалення таблиць у правильному порядку 
DROP TABLE IF EXISTS `payment`;
DROP TABLE IF EXISTS `package_tracking`;
DROP TABLE IF EXISTS `packages`;
DROP TABLE IF EXISTS `courier_branches`;
DROP TABLE IF EXISTS `branches_senders`;
DROP TABLE IF EXISTS `couriers`;
DROP TABLE IF EXISTS `senders`;
DROP TABLE IF EXISTS `receivers`;
DROP TABLE IF EXISTS `delivery_address`;
DROP TABLE IF EXISTS `postmats`;
DROP TABLE IF EXISTS `branches`;
DROP TABLE IF EXISTS `operating_hours`;

-- 3. Створення таблиць
CREATE TABLE IF NOT EXISTS `operating_hours` (
  hours_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  day VARCHAR(50) NOT NULL,
  open_time TIME NOT NULL,
  close_time TIME NOT NULL,
  UNIQUE KEY `idx_day_open_close` (`day`, `open_time`, `close_time`)
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

CREATE TABLE IF NOT EXISTS `branches` (
  branch_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  branch_ip VARCHAR(25) NOT NULL,
  address VARCHAR(255) NOT NULL,
  hours_id INT NOT NULL,
  phone VARCHAR(20) NOT NULL
  
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

CREATE TABLE IF NOT EXISTS `senders` (
  sender_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  full_name VARCHAR(100) NOT NULL,
  phone VARCHAR(20) NOT NULL,
  email VARCHAR(100) NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

CREATE TABLE IF NOT EXISTS `branches_senders` (
  branch_id INT NOT NULL,
  sender_id INT NOT NULL,
  PRIMARY KEY (branch_id, sender_id)
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

CREATE TABLE IF NOT EXISTS `couriers` (
  courier_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  phone VARCHAR(15) NOT NULL,
  vehicle_type ENUM('Car', 'Bike', 'Van') NOT NULL,
  UNIQUE KEY `idx_courier_phone` (`phone`)
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

CREATE TABLE IF NOT EXISTS `courier_branches` (
  courier_id INT NOT NULL,
  branch_id INT NOT NULL,
  PRIMARY KEY (courier_id, branch_id)
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

CREATE TABLE IF NOT EXISTS `delivery_address` (
  address_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  address VARCHAR(255) NOT NULL,
  delivery_instructions VARCHAR(250) NOT NULL,
  UNIQUE KEY `idx_address` (`address`)
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

CREATE TABLE IF NOT EXISTS `receivers` (
  receiver_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  phone VARCHAR(15) NOT NULL,
  email VARCHAR(100) NOT NULL,
  UNIQUE KEY `idx_receiver_phone` (`phone`),
  UNIQUE KEY `idx_receiver_email` (`email`)
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

CREATE TABLE IF NOT EXISTS `packages` (
  package_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  sender_id INT NOT NULL,
  receiver_id INT NOT NULL,
  delivery_address_id INT NOT NULL,
  description TEXT NOT NULL,
  weight DECIMAL(5, 2) NOT NULL,
  status VARCHAR(20) NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

CREATE TABLE IF NOT EXISTS `package_tracking` (
  tracking_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  package_id INT NOT NULL,
  branch_id INT NOT NULL,
  status VARCHAR(20) NOT NULL,
  timestap DATETIME NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

CREATE TABLE IF NOT EXISTS `postmats` (
  postmat_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  location VARCHAR(255) NOT NULL,
  status VARCHAR(20) NOT NULL,
  branch_id INT NOT NULL,
  UNIQUE KEY `idx_postmat_location` (`location`)
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

CREATE TABLE IF NOT EXISTS `payment` (
  payment_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  package_id INT NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  payment_date DATE NOT NULL,
  payment_status ENUM('Pending', 'Paid', 'Failed') NOT NULL
) ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

-- 4. Додавання зовнішніх ключів за допомогою ALTER TABLE
ALTER TABLE `branches`
  ADD CONSTRAINT FK_branches_hours FOREIGN KEY (`hours_id`) REFERENCES `operating_hours`(`hours_id`) ON DELETE CASCADE;

ALTER TABLE `branches_senders`
  ADD CONSTRAINT FK_branches_senders_branch FOREIGN KEY (`branch_id`) REFERENCES `branches`(`branch_id`) ON DELETE CASCADE,
  ADD CONSTRAINT FK_branches_senders_sender FOREIGN KEY (`sender_id`) REFERENCES `senders`(`sender_id`) ON DELETE CASCADE;

ALTER TABLE `courier_branches`
  ADD CONSTRAINT FK_courier_branches_courier FOREIGN KEY (`courier_id`) REFERENCES `couriers`(`courier_id`) ON DELETE CASCADE,
  ADD CONSTRAINT FK_courier_branches_branch FOREIGN KEY (`branch_id`) REFERENCES `branches`(`branch_id`) ON DELETE CASCADE;

ALTER TABLE `packages`
  ADD CONSTRAINT FK_packages_sender FOREIGN KEY (`sender_id`) REFERENCES `senders`(`sender_id`) ON DELETE CASCADE,
  ADD CONSTRAINT FK_packages_receiver FOREIGN KEY (`receiver_id`) REFERENCES `receivers`(`receiver_id`) ON DELETE CASCADE,
  ADD CONSTRAINT FK_packages_address FOREIGN KEY (`delivery_address_id`) REFERENCES `delivery_address`(`address_id`) ON DELETE CASCADE;

ALTER TABLE `package_tracking`
  ADD CONSTRAINT FK_package_tracking_package FOREIGN KEY (`package_id`) REFERENCES `packages`(`package_id`) ON DELETE CASCADE,
  ADD CONSTRAINT FK_package_tracking_branch FOREIGN KEY (`branch_id`) REFERENCES `branches`(`branch_id`) ON DELETE CASCADE;

ALTER TABLE `postmats`
  ADD CONSTRAINT FK_postmats_branch FOREIGN KEY (`branch_id`) REFERENCES `branches`(`branch_id`) ON DELETE CASCADE;


  -- Inserts Datas into Tables

START TRANSACTION;
USE Tracking_sql;
INSERT INTO `operating_hours` (hours_id, day, open_time, close_time) VALUES 
(1, 'Monday-Saturday', '09:00:00', '19:00:00'),
(2, 'Tuesday-Sunday', '09:00:00', '17:00:00'),
(3, 'Monday-Friday', '10:00:00', '20:00:00'),
(4, 'Thursday-Sunday', '09:00:00', '18:00:00'),
(5, 'Thursday-Saturday', '09:00:00', '20:00:00'),
(6, 'Sunday-Thursday', '09:00:00', '15:00:00'),
(7, 'Monday-Wednesday', '10:00:00', '18:00:00'),
(8, 'Tuesday-Thursday', '11:00:00', '19:00:00'),
(9, 'Friday-Sunday', '12:00:00', '20:00:00'),
(10, 'Saturday-Wednesday', '08:00:00', '14:00:00');

COMMIT;


START TRANSACTION;
USE Tracking_sql;
INSERT INTO `branches` (branch_id, branch_ip, address, hours_id, phone) VALUES 
(1, '192.168.1.1', '123 Shevchenka Blvd, Kyiv', 1, '+380631234567'),
(2, '193.168.1.2', '45K Hrushevskoho St, Lviv', 2, '+380552345678'),
(3, '194.168.1.3', '78A Deribasovska St, Odesa', 3, '+380683456789'),
(4, '191.168.1.4', '321 Pushkinska St, Kharkiv', 5, '+380734567890'),
(5, '197.168.1.5', '65E Main St, Dnipro', 4, '+380975678901'),
(6, '198.168.1.6', '98B Victory Ave, Zaporizhzhia', 7, '+380986789012'),
(7, '192.168.1.7', '135 T. Shevchenka St, Ivano-Frankivsk', 10, '+380937890123'),
(8, '193.168.2.1', '101 High St, Kyiv', 5, '+380701112233'),
(9, '196.168.2.2', '202 Rynok Sq, Lviv', 6, '+380732223344'),
(10, '195.168.2.3', '303 Park Ave, Odesa', 8, '+380523334455'),
(11, '192.168.2.4', '40C Elm St, Kharkiv', 2, '+380504445566'),
(12, '190.168.2.5', '50T Maple Ave, Dnipro', 10, '+380565556677'),
(13, '197.168.1.6', '12А Cerkovna St, Sambir', '9', '+380673822123');

COMMIT;


START TRANSACTION;
USE Tracking_sql;
INSERT INTO `senders` (sender_id, full_name, phone, email) VALUES 
(1, 'Ivan Petrenko', '+380631234567', 'ivan.petrenko@gmail.com'),
(2, 'Olena Shevchenko', '+380552345678', 'olena.shevchenko@gmail.com'),
(3, 'Pavlo Kovalenko', '+380683456789', 'pavlo.kovalenko@gmail.com'),
(4, 'Neonila Dibrova', '+380734567890', 'nina.dibrova@gmail.com'),
(5, 'Andriy Melnyk', '+380975678901', 'andriy.melnyk@gmail.com'),
(6, 'Maria Ivanyk', '+380986789012', 'maria.ivanyk@gmail.com'),
(7, 'Serhiy Tarasenko', '+380937890123', 'serhiy.tarasenko@gmail.com'),
(8, 'Oleksiy Honchar', '+380701112233', 'oleksiy.honchar@gmail.com'),
(9, 'Inna Ivanyuk', '+380732223344', 'inna.ivanyuk@gmail.com'),
(10, 'Taras Shevchuk', '+380523334455', 'taras.shevchuk@gmail.com'),
(11, 'Olga Demchenko', '+380504445566', 'olga.demchenko@gmail.com');

COMMIT;


START TRANSACTION;
USE Tracking_sql;
INSERT INTO `branches_senders` (branch_id, sender_id) VALUES 
(1, 2),
(2, 1),
(3, 6),
(4, 2),
(5, 5),
(6, 9),
(7, 4),
(8, 3),
(9, 3),
(10, 11),
(11, 10),
(12, 7),
(13, 8),
(9, 4),
(2, 6),
(6, 7),
(12, 11);

COMMIT;


START TRANSACTION;
USE Tracking_sql;
INSERT INTO `couriers` (courier_id, name, phone, vehicle_type) VALUES 
(1, 'Pavlo Melnyk', '+380673456789', 'Car'),
(2, 'Iryna Petrenko', '+380684567890', 'Bike'),
(3, 'Oleksiy Ivanov', '+380635678901', 'Van'),
(4, 'Anna Hrytsenko', '+380506789012', 'Car'),
(5, 'Serhiy Popov', '+380967890123', 'Bike'),
(6, 'Olga Moroz', '+380448901234', 'Van'),
(7, 'Dmytro Yakovlev', '+380679012345', 'Car'),
(8, 'Artem Kravets', '+380671122334', 'Car'),
(9, 'Viktoria Dotsenko', '+380682233445', 'Bike'),
(10, 'Maksym Holub', '+380633344556', 'Van'),
(11, 'Oksana Nikolenko', '+380504455667', 'Car');

COMMIT;


START TRANSACTION;
USE Tracking_sql;
INSERT INTO `courier_branches` (courier_id, branch_id) VALUES 
(1, 1),
(2, 1),
(3, 2),
(4, 2),
(5, 4),
(6, 5),
(7, 6),
(8, 2),
(9, 3),
(10, 5),
(11, 7),
(3, 13),
(1, 8),
(9, 11),
(10, 10),
(5, 12);

COMMIT;


START TRANSACTION;
USE Tracking_sql;
INSERT INTO `delivery_address` (address_id, address, delivery_instructions) VALUES 
(1, '123 Shevchenko Ave, Kyiv', 'Leave at security desk'),
(2, '45 Khmelnytsky Blvd, Lviv', 'Ring twice at door'),
(3, '67 Lesya St, Odesa', 'Deliver to front office'),
(4, '98 Franko Rd, Kharkiv', 'Leave at reception'),
(5, '200 Sichovykh Striltsiv Lane, Dnipro', 'Call before arriving'),
(6, '89 Poltava Rd, Zaporizhzhia', 'Handle with care'),
(7, '132 Independence Blvd, Ivano-Frankivsk', 'Leave at the back door'),
(8, '45 Bohdan Khmelnytsky Ave, Kyiv', 'Ring the bell once'),
(9, '150 Lypynsky St, Lviv', 'Contact on arrival'),
(10, '77 Deribasivska St, Odesa', 'Leave package in lobby'),
(11, '110 Vernadskiy Rd, Kharkiv', 'Deliver to main entrance'),
(12, '220 Yavornytsky Ave, Dnipro', 'Use side door for delivery');

COMMIT;


START TRANSACTION;
USE Tracking_sql;
INSERT INTO `receivers` (receiver_id, name, phone, email) VALUES 
(1, 'Borys Andriyenko', '+380501112223', 'borys.andriyenko@gmail.com'),
(2, 'Larysa Kuznetsova', '+380672345678', 'larysa.kuznetsova@ukr.net'),
(3, 'Roman Levchenko', '+380633334445', 'roman.levchenko@gmail.com'),
(4, 'Oksana Hladka', '+380954567890', 'oksana.hladka@ukr.net'),
(5, 'Andriy Tkachenko', '+380665678901', 'andriy.tkachenko@gmail.com'),
(6, 'Svitlana Polishchuk', '+380936789012', 'svitlana.polishchuk@ukr.net'),
(7, 'Yuriy Kovalenko', '+380967890123', 'yuriy.kovalenko@gmail.com'),
(8, 'Nadia Melnyk', '+380678901234', 'nadia.melnyk@ukr.net'),
(9, 'Vadym Ostapenko', '+380689012345', 'vadym.ostapenko@gmail.com'),
(10, 'Iryna Mykolaivna', '+380501122334', 'iryna.mykolaivna@ukr.net'),
(11, 'Petro Shulha', '+380972233445', 'petro.shulha@gmail.com'),
(12, 'Olha Shostak', '+380633344556', 'olha.shostak@ukr.net');

COMMIT;


START TRANSACTION;
USE Tracking_sql;

INSERT INTO `packages` (package_id, sender_id, receiver_id, delivery_address_id, description, weight, status) VALUES 
(1, 1, 3, 2, 'Household goods', 10.50, 'In Transit'),
(2, 3, 5, 7, 'Office supplies', 5.75, 'Delivered'),
(3, 2, 4, 10, 'Electronics', 2.25, 'Pending'),
(4, 4, 1, 5, 'Furniture', 50.00, 'In Transit'),
(5, 7, 8, 3, 'Medical equipment', 12.80, 'Delivered'),
(6, 9, 12, 6, 'Groceries', 8.20, 'Pending'),
(7, 8, 9, 4, 'Clothing', 4.00, 'In Transit'),
(8, 10, 2, 9, 'Stationery', 3.25, 'Delivered'),
(9, 6, 7, 11, 'Art supplies', 6.30, 'Pending'),
(10, 5, 11, 12, 'Books and media', 7.50, 'In Transit'),
(11, 8, 6, 8, 'Toys and games', 9.70, 'Delivered'),
(12, 11, 10, 1, 'Kitchen items', 11.45, 'Pending'),
(13, 2, 3, 6, 'Sporting goods', 15.60, 'In Transit'),
(14, 1, 5, 3, 'Automotive parts', 18.20, 'Delivered'),
(15, 4, 7, 10, 'Camping equipment', 22.00, 'Pending'),
(16, 6, 9, 4, 'Tools and hardware', 25.50, 'In Transit');

COMMIT;



START TRANSACTION;
USE Tracking_sql;
INSERT INTO `package_tracking` (tracking_id, package_id, branch_id, status, timestap) VALUES 
(1, 1, 1, 'Received', '2024-09-02 10:00:00'),  
(2, 2, 3, 'In Transit', '2024-09-02 12:45:00'),  
(3, 3, 5, 'Pending', '2024-09-03 08:30:00'),  
(4, 4, 7, 'Pending', '2024-09-03 17:20:00'),  
(5, 5, 9, 'In Transit', '2024-09-04 11:15:00'),  
(6, 6, 11, 'Received', '2024-09-05 09:50:00'),  
(7, 7, 2, 'Out for Delivery', '2024-09-05 13:40:00'),  
(8, 8, 4, 'Delivered', '2024-09-06 15:25:00'),  
(9, 9, 6, 'Received', '2024-09-07 10:05:00'),  
(10, 10, 8, 'Pending', '2024-09-08 14:35:00'),  
(11, 11, 10, 'Out for Delivery', '2024-09-09 13:00:00'),  
(12, 12, 12, 'Pending', '2024-09-10 09:25:00'),  
(13, 13, 3, 'In Transit', '2024-09-11 11:15:00'),  
(14, 14, 5, 'Pending', '2024-09-12 10:45:00'),  
(15, 15, 7, 'Delivered', '2024-09-13 12:00:00'),  
(16, 16, 2, 'In Transit', '2024-09-14 10:00:00');  
COMMIT;



START TRANSACTION;
USE Tracking_sql;
INSERT INTO `postmats` (postmat_id, location, status, branch_id) VALUES 
(1, 'Main Station Postmat, Kyiv', 'Active', 1),
(2, 'Central Postmat, Lviv', 'Inactive', 2),
(3, 'South Odesa Postmat', 'Active', 4),
(4, 'Downtown Postmat, Kharkiv', 'Maintenance', 6),
(5, 'North Dnipro Postmat', 'Active', 8),
(6, 'Center Zaporizhzhia Postmat', 'Inactive', 9),
(7, 'West Ivano-Frankivsk Postmat', 'Active', 3),
(8, 'High St Postmat, Kyiv', 'Active', 5),
(9, 'Rynok Postmat, Lviv', 'Maintenance', 7),
(10, 'East Odesa Postmat', 'Active', 10),
(11, 'Elm St Postmat, Kharkiv', 'Inactive', 11),
(12, 'Maple Ave Postmat, Dnipro', 'Active', 12),
(13, 'Shevchenko Blvd Postmat, Kyiv', 'Active', 1),
(14, 'Independence Ave Postmat, Lviv', 'Active', 2),
(15, 'Victory Ave Postmat, Zaporizhzhia', 'Inactive', 6);

COMMIT;

START TRANSACTION;
USE Tracking_sql;
INSERT INTO `payment` (payment_id, package_id, amount, payment_date, payment_status) VALUES 
(1, 1, 100.00, '2024-09-01', 'Paid'),
(2, 2, 75.50, '2024-09-02', 'Paid'),
(3, 3, 200.25, '2024-09-03', 'Pending'),
(4, 4, 150.00, '2024-09-03', 'Failed'),
(5, 5, 300.80, '2024-09-04', 'Paid'),
(6, 6, 120.20, '2024-09-05', 'Paid'),
(7, 7, 50.00, '2024-09-05', 'Pending'),
(8, 8, 30.25, '2024-09-06', 'Paid'),
(9, 9, 70.30, '2024-09-07', 'Pending'),
(10, 10, 90.00, '2024-09-08', 'Pending'),
(11, 11, 40.70, '2024-09-09', 'Paid'),
(12, 12, 110.45, '2024-09-10', 'Pending'),
(13, 13, 150.60, '2024-09-11', 'Paid'),
(14, 14, 180.20, '2024-09-12', 'Failed'),
(15, 15, 220.00, '2024-09-13', 'Paid'),
(16, 16, 250.50, '2024-09-14', 'Paid');

COMMIT;
