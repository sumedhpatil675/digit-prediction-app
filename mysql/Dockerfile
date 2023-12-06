# Use the official MySQL image as a parent image
FROM mysql:latest

# Add the initialization SQL script to the container
ADD init.sql /docker-entrypoint-initdb.d
