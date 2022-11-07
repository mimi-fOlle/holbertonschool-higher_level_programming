-- Create the database hbtn_0d_2 and the user_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'hbtn_0d_2';
GRANT SELECT ON *.* TO 'user_0d_2'@'hbtn_0d_2';
ALTER USER 'user_0d_2'@'hbtn_0d_2' IDENTIFIED BY 'user_0d_2_pwd';
