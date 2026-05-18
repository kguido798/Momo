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
