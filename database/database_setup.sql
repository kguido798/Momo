CREATE DATABASE momo_sms_db;
USE momo_sms_db;
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(10) NOT NULL UNIQUE,
    email VARCHAR(50),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,);
CREATE TABLE accounts (
    account_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    balance DECIMAL(12,2) DEFAULT 0.00,
    account_type VARCHAR(50) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,    
    FOREIGN KEY (user_id) REFERENCES users(user_id));
CREATE TABLE transaction_categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL UNIQUE,);
CREATE TABLE transaction_status (
    status_id INT AUTO_INCREMENT PRIMARY KEY,  
    status_name VARCHAR(30) NOT NULL UNIQUE);
CREATE TABLE transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    status_id INT NOT NULL,
    amount DECIMAL(12,2) NOT NULL,
    transaction_reference VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    transaction_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES transaction_categories(category_id),    
    FOREIGN KEY (status_id) REFERENCES transaction_status(status_id));
CREATE TABLE transaction_participants (
    participant_id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_id INT NOT NULL,
    user_id INT NOT NULL,
    role ENUM('Sender', 'Receiver', 'Agent') NOT NULL,
    FOREIGN KEY (transaction_id) REFERENCES transactions(transaction_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id));
CREATE TABLE system_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_id INT,
    log_level ENUM('INFO', 'WARNING', 'ERROR') NOT NULL,
    message TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (transaction_id) REFERENCES transactions(transaction_id));
CREATE INDEX idx_phone_number ON users(phone_number);
CREATE INDEX idx_transaction_date ON transactions(transaction_date);
CREATE INDEX idx_category_id ON transactions(category_id);
INSERT INTO users(full_name, phone_number, email) VALUES
('Rene Guido', '0791059888', 'g.kayigamba@alustudent.com'),
('Elijah Kabatsi', '0783339542', 'e.kabatsi@alustudent.com'),
('Yves Nyirihirwe', '0791992053', 'n.yves@alustudent.com'),
('Yann Kanjogera', '0782990117', 'y.kanjogera@alustudent.com'),
('Chris Tucker', '0787938467', 't.chris@alustudent.com');
INSERT INTO transaction_categories(category_name) VALUES
('Transfer'),
('Airtime'),
('Cash Out'),
('Bill Payment'),
('Merchant Payment');
INSERT INTO transaction_status(status_name) VALUES
('Successful'),
('Pending'),
('Failed');
INSERT INTO transactions( category_id, status_id, amount, transaction_reference, description
) VALUES
(1,1,2500,'TXN001','Transfer to Jane'),
(2,2,1000,'TXN002','Airtime purchase'),
(3,3,5000,'TXN003','Cash withdrawal'),
(4,4,7500,'TXN004','Electricity payment'),
(5,5,3000,'TXN005','Merchant payment');
INSERT INTO transaction_participants( transaction_id, user_id, role) VALUES
(1,1,'Sender'),
(1,2,'Receiver'),
(2,3,'Sender'),
(3,4,'Sender'),
(4,5,'Receiver');
INSERT INTO system_logs( transaction_id, log_level,  message)VALUES
    (1,'INFO','Transaction completed'),
    (2,'INFO','Airtime successful'),
    (3,'WARNING','Pending approval'),
    (4,'INFO','Bill paid'),
    (5,'ERROR','Merchant payment failed');
