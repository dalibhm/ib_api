wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
# sudo apt-get install gnupg
echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
apt update
apt-get install -y mongodb-org

