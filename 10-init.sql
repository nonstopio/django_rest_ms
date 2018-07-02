create database team_db;
\c team_db;
create user team_ms_user with password 'team_ms123';
ALTER ROLE team_ms_user SET client_encoding TO 'utf8';
ALTER ROLE team_ms_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE team_ms_user SET timezone TO 'Asia/Kolkata';
GRANT ALL PRIVILEGES ON DATABASE team_db TO team_ms_user;
