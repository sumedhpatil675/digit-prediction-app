-- Create a database and user for the Flask app
CREATE DATABASE IF NOT EXISTS prediction_db;

-- Change 'root' to the desired username for your Flask app
-- Change 'localhost' to '%' to allow connections from any host (or specify a specific host)
-- GRANT ALL PRIVILEGES ON prediction_db.* TO 'root'@'%' IDENTIFIED BY 'password';
