CREATE DATABASE personal_safety; 

USE personal_safety;

CREATE TABLE alerts (
    id INT PRIMARY KEY,
    message VARCHAR(25)
);

CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(25),
    email VARCHAR(25),
    password VARCHAR(25)
);


CREATE TABLE locations (
    id INT PRIMARY KEY,
    user_id INT,
    latitude FLOAT,
    longitude FLOAT,
    timestamp DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE contacts (
    id INT PRIMARY KEY,
    user_id INT,
    contact_name VARCHAR(25),
    contact_number VARCHAR(15),
    FOREIGN KEY (user_id) REFERENCES users(id)
);


CREATE TABLE emergency_services (
    id INT PRIMARY KEY,
    service_name VARCHAR(25),
    contact_number VARCHAR(15)
);


