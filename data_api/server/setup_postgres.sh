psql -h <host> -p <port> -U <username> -W <password> <database>
sudo apt install postgresql-client-common
sudo apt-get install postgresql-client

sudo psql -U mohamedali_benhamouda_gcp  -h 35.197.213.163 -W vKr33HKrIoHA10DK
postgres=# create database ib;
postgres=# create user api with encrypted password 'api_pass198753hcou329h2rcou97g BTBN*FG*';
postgres=# grant all privileges on database ib to api;