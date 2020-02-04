echo 'deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main' > sudo /etc/apt/sources.list.d/pgdg.list
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update

apt-get install postgresql-11

su postgres
/usr/lib/postgresql/11/bin/pg_ctl initdb --pgdata=/data/postgresql

sudo -u postgres psql

postgres=# create database stock_db;
postgres=# create user ib_integration with password 'ib_integration';
postgres=# grant all privileges on database stock_db to ib_integration;