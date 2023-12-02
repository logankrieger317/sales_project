-- settings.sql
CREATE DATABASE sales;
CREATE USER salesuser WITH PASSWORD 'sales';
GRANT ALL PRIVILEGES ON DATABASE sales TO salesuser;