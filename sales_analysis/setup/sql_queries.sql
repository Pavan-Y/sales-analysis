CREATE TABLE IF NOT EXISTS product_staging_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    file_name VARCHAR(255),
    file_location VARCHAR(255),
    created_date TIMESTAMP ,
    updated_date TIMESTAMP ,
    status VARCHAR(1)
);

CREATE TABLE IF NOT EXISTS customer (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    address VARCHAR(255),
    pincode VARCHAR(10),
    phone_number VARCHAR(20),
    customer_joining_date DATE
);


INSERT INTO customer (first_name, last_name, address, pincode, phone_number, customer_joining_date)
VALUES
    ('Vikram', 'Rao', '102, MG Road, Bangalore, 560001', '560001', '91-9123456789', '2023-11-18'),
    ('Priya', 'Sharma', '504, Marathalli, Chennai, 600001', '600001', '91-9988776655', '2023-11-18'),
    ('Karan', 'Singh', '301, Rajouri Garden, New Delhi, 110027', '110027', '91-9876543210', '2023-11-18'),
    ('Pooja', 'Patel', '45, Malviya Nagar, Jaipur, 302017', '302017', '91-9333333333', '2023-11-18'),
    ('Rohan', 'Kumar', '703, Koramangala, Bangalore, 560034', '560034', '91-9444444444', '2023-11-18'),
    ('Neha', 'Rao', '805, Indiranagar, Lucknow, 226001', '226001', '91-9555555555', '2023-11-18'),
    ('Amit', 'Joshi', '12, Gomti Nagar, Lucknow, 226010', '226010', '91-9666666666', '2023-11-18'),
    ('Anjali', 'Malhotra', '22, Vaishali Nagar, Jaipur, 302021', '302021', '91-9777777777', '2023-11-18'),
    ('Rahul', 'Verma', '1001, Shivaji Nagar, Pune, 411005', '411005', '91-9888888888', '2023-11-18'),
    ('Aditi', 'Shah', '705, Andheri West, Mumbai, 400053', '400053', '91-9222222222', '2023-11-18'),
    ('Raj', 'Pandey', '301, Baner, Pune, 411045', '411045', '91-9333312345', '2023-11-18'),
    ('Sakshi', 'Goyal', '110, Rajkot Road, Ahmedabad, 380006', '380006', '91-9111111111', '2023-11-18'),
    ('Rishi', 'Jain', '405, Civil Lines, Nagpur, 440001', '440001', '91-9444477777', '2023-11-18'),
    ('Sonia', 'Singhal', '201, Dehradun Road, Rishikesh, 249201', '249201', '91-9666612345', '2023-11-18'),
    ('Rajat', 'Goswami', '908, Kanpur Road, Lucknow, 226018', '226018', '91-9777733333', '2023-11-18'),
    ('Isha', 'Mishra', '401, Gwalior Road, Agra, 282001', '282001', '91-9555533333', '2023-11-18'),
    ('Rohan', 'Chauhan', '605, Kalyanpur, Kanpur, 208017', '208017', '91-9444441234', '2023-11-18'),
    ('Shreya', 'Thakur', '302, Chandigarh Enclave, Chandigarh, 160017', '160017', '91-9777771234', '2023-11-18'),
    ('Raj', 'Saxena', '28, Vijay Nagar, Indore, 452010', '452010', '91-9666612345', '2023-11-18'),
    ('Aditya', 'Rawat', '706, Haridwar Road, Dehradun, 248001', '248001', '91-9333333456', '2023-11-18'),
    ('Riyaan', 'Gandhi', '901, Patna City, Patna, 800008', '800008', '91-9111112345', '2023-11-18'),
    ('Avani', 'Iyer', '1001, Kochi Lane, Kochi, 682001', '682001', '91-9444477777', '2023-11-18'),
    ('Reyansh', 'Reddy', '1503, Kondapur, Hyderabad, 500084', '500084', '91-9555512345', '2023-11-18'),
    ('Aadhya', 'Menon', '200, Calicut Road, Kozhikode, 673001', '673001', '91-9888812345', '2023-11-18'),
    ('Ishita', 'Pillai', '503, Alappuzha, Alappuzha, 688001', '688001', '91-9666612345', '2023-11-18'),
    ('Arjun', 'Menon', '1102, Mangalore, Mangalore, 575001', '575001', '91-9555512345', '2023-11-18'),
    ('Aarav', 'Pai', '1201, Panaji, Panaji, 403001', '403001', '91-9333312345', '2023-11-18'),
    ('Ishaan', 'Menon', '1705, Nashik Road, Nashik, 422001', '422001', '91-9888812345', '2023-11-18'),
    ('Ananya', 'Shah', '1401, Vadodara, Vadodara, 390001', '390001', '91-9777712345', '2023-11-18'),
    ('Aadhya', 'Menon', '1602, Surat, Surat, 395001', '395001', '91-9555512345', '2023-11-18'),
    ('Aaliyah', 'Rao', '1803, Rajkot, Rajkot, 360001', '360001', '91-9444412345', '2023-11-18'),
    ('Aarush', 'Nair', '1504, Kochi, Kochi, 682001', '682001', '91-9333312345', '2023-11-18'),
    ('Aarav', 'Iyer', '1902, Kozhikode, Kozhikode, 673001', '673001', '91-9888812345', '2023-11-18'),
    ('Rahul', 'Pillai', '2001, Thrissur, Thrissur, 680001', '680001', '91-9355531234', '2023-11-18'),
    ('Reyansh', 'Kumar', '501, Velachery, Chennai, 600042', '600042', '91-9777123456', '2023-11-18'),
    ('Arnav', 'Sharma', '302, Kothrud, Pune, 411029', '411029', '91-9555123456', '2023-11-18'),
    ('Anika', 'Gupta', '501, Malad West, Mumbai, 400064', '400064', '91-9888898765', '2023-11-18'),
    ('Saanvi', 'Verma', '1202, Adyar, Chennai, 600020', '600020', '91-9666698765', '2023-11-18'),
    ('Shaurya', 'Chauhan', '1101, Connaught Place, New Delhi, 110001', '110001', '91-9444478765', '2023-11-18'),
    ('Anaya', 'Shah', '601, Jayanagar, Bangalore, 560041', '560041', '91-9555532345', '2023-11-18'),
    ('Yash', 'Patil', '1202, Andheri East, Mumbai, 400069', '400069', '91-9333345678', '2023-11-18'),
    ('Vihaan', 'Singh', '2002, Shivajinagar, Pune, 411005', '411005', '91-9666662345', '2023-11-18'),
    ('Aayat', 'Rao', '301, Koramangala, Bangalore, 560034', '560034', '91-9888898765', '2023-11-18'),
    ('Shaurya', 'Iyer', '703, MG Road, Mumbai, 400001', '400001', '91-9777787654', '2023-11-18'),
    ('Zoya', 'Chauhan', '1402, Indiranagar, Bangalore, 560008', '560008', '91-9444498765', '2023-11-18'),
    ('Kabir', 'Sharma', '1602, Sadashivnagar, Bangalore, 560080', '560080', '91-9111123456', '2023-11-18'),
    ('Vihaan', 'Jain', '1402, Rajouri Garden, New Delhi, 110027', '110027', '91-9888887654', '2023-11-18'),
    ('Kiara', 'Shah', '701, Malviya Nagar, Jaipur, 302017', '302017', '91-9777772345', '2023-11-18'),
    ('Kiaan', 'Kumar', '901, Koramangala, Bangalore, 560034', '560034', '91-9555523456', '2023-11-18'),
    ('Sara', 'Rao', '402, Malad West, Mumbai, 400064', '400064', '91-9333312345', '2023-11-18');

CREATE TABLE IF NOT EXISTS store (
    id INT PRIMARY KEY,
    address VARCHAR(255),
    store_pincode VARCHAR(10),
    store_manager_name VARCHAR(100),
    store_opening_date DATE,
    reviews TEXT
);

INSERT INTO store (id, address, store_pincode, store_manager_name, store_opening_date, reviews)
VALUES
    ('901','Delhi', '122009', 'Manish', '2022-01-15', 'Great store with a friendly staff.'),
    ('902','Delhi', '110011', 'Nikita', '2021-08-10', 'Excellent selection of products.'),
    ('903','Delhi', '201301', 'Vikash', '2023-01-20', 'Clean and organized store.'),
    ('904','Delhi', '400001', 'Rakesh', '2020-05-05', 'Good prices and helpful staff.'),
    ('905','Mumbai', '400010', 'Priya', '2023-06-12', 'Wonderful shopping experience.'),
    ('906','Bangalore', '560001', 'Karthik', '2021-12-25', 'Helpful and knowledgeable staff.'),
    ('907','Chennai', '600001', 'Aditi', '2020-10-30', 'Great variety and quality products.'),
    ('908','Pune', '411001', 'Rahul', '2022-09-17', 'Convenient location and good prices.'),
    ('909','Hyderabad', '500001', 'Sanjay', '2021-05-08', 'Fantastic customer service.'),
    ('910','Kolkata', '700001', 'Amit', '2023-03-20', 'Always fresh products available.'),
    ('911','Ahmedabad', '380001', 'Riya', '2020-11-22', 'Friendly and helpful staff.'),
    ('912','Jaipur', '302001', 'Arun', '2022-07-14', 'Highly recommended for quality.'),
    ('913','Chandigarh', '160001', 'Raj', '2023-08-05', 'Amazing deals and discounts.'),
    ('914','Lucknow', '226001', 'Neha', '2021-04-30', 'Clean and well-organized store.'),
    ('915','Patna', '800001', 'Sagar', '2020-02-18', 'Great selection of products and prices.');


CREATE TABLE IF NOT EXISTS product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    current_price DECIMAL(10, 2),
    old_price DECIMAL(10, 2),
    created_date TIMESTAMP ,
    updated_date TIMESTAMP ,
    expiry_date DATE
);


INSERT INTO product (name, current_price, old_price, created_date, updated_date, expiry_date)
VALUES
    ('apple', 100, 212, '2022-05-15', NULL, '2025-01-01'),
    ('banana', 20, 50, '2021-08-10', NULL, '2025-01-01'),
    ('orange', 30, 20, '2023-03-20', NULL, '2025-01-01'),
    ('bread', 50, 52, '2020-05-05', NULL, '2025-01-01'),
    ('milk', 150, 110, '2022-01-15', NULL, '2025-01-01'),
    ('cheese', 300, 150, '2021-09-25', NULL, '2025-01-01'),
    ('lettuce', 80, 100, '2023-07-10', NULL, '2025-01-01'),
    ('chicken', 250, 200, '2020-11-30', NULL, '2025-01-01'),
    ('rice', 100, 120, '2021-11-30', NULL, '2025-01-01'),
    ('tomato', 45, 60, '2022-11-30', NULL, '2025-01-01');


CREATE TABLE IF NOT EXISTS sales_team (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    manager_id INT,
    is_manager CHAR(1),
    address VARCHAR(255),
    pincode VARCHAR(10),
    joining_date DATE
);

INSERT INTO sales_team (first_name, last_name, manager_id, is_manager, address, pincode, joining_date)
VALUES
    ('Rahul', 'Verma', 10, 'N', 'Delhi', '122007', '2020-05-01'),
    ('Priya', 'Singh', 10, 'N', 'Delhi', '122007', '2020-05-01'),
    ('Amit', 'Sharma', 10, 'N', 'Delhi', '122007', '2020-05-01'),
    ('Sneha', 'Gupta', 10, 'N', 'Delhi', '122007', '2020-05-01'),
    ('Neha', 'Kumar', 10, 'N', 'Delhi', '122007', '2020-05-01'),
    ('Vijay', 'Yadav', 10, 'N', 'Delhi', '122007', '2020-05-01'),
    ('Anita', 'Malhotra', 10, 'N', 'Delhi', '122007', '2020-05-01'),
    ('Alok', 'Rajput', 10, 'N', 'Delhi', '122007', '2020-05-01'),
    ('Monica', 'Jain', 10, 'N', 'Delhi', '122007', '2020-05-01'),
    ('Rajesh', 'Gupta', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Suresh', 'Singh', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Nisha', 'Verma', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Arun', 'Sharma', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Riya', 'Gupta', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Sanjay', 'Kumar', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Kiran', 'Singh', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Mohan', 'Verma', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Pooja', 'Sharma', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Sarita', 'Gupta', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Anil', 'Rajput', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Deepak', 'Jain', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Rahul', 'Sharma', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Preeti', 'Verma', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Anjali', 'Singh', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Sushil', 'Gupta', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Manoj', 'Kumar', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Vidya', 'Sharma', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Gopal', 'Yadav', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Vijay', 'Rajput', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Ashok', 'Verma', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Anu', 'Sharma', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Aarti', 'Gupta', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Rajiv', 'Kumar', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Rohit', 'Singh', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Renu', 'Verma', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Anushka', 'Sharma', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Mukesh', 'Gupta', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Seema', 'Yadav', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Rajni', 'Rajput', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Sonu', 'Verma', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Jyoti', 'Sharma', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Ramesh', 'Kumar', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Nisha', 'Singh', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Ajay', 'Verma', 10, 'Y', 'Delhi', '122007', '2020-05-01'),
    ('Rajesh', 'Gupta', 10, 'Y', 'Delhi', '122007', '2020-05-01');


CREATE TABLE IF NOT EXISTS s3_bucket_info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    bucket_name VARCHAR(255),
    file_location VARCHAR(255),
    created_date TIMESTAMP ,
    updated_date TIMESTAMP ,
    status VARCHAR(20)
);


INSERT INTO s3_bucket_info (bucket_name, status, created_date, updated_date)
VALUES ('my-bucket-name', 'active', NOW(), NOW());



CREATE TABLE  IF NOT EXISTS customers_data_mart (
    customer_id INT ,
    full_name VARCHAR(100),
    address VARCHAR(200),
    phone_number VARCHAR(20),
    sales_date_month VARCHAR(7),
    total_sales DECIMAL(10, 2)
);


CREATE TABLE IF NOT EXISTS sales_team_data_mart (
    store_id INT,
    sales_person_id INT,
    full_name VARCHAR(255),
    sales_month VARCHAR(10),
    total_sales DECIMAL(10, 2),
    incentive DECIMAL(10, 2)
);