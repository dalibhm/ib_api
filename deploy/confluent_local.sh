sudo apt install curl
curl -O http://packages.confluent.io/archive/5.3/confluent-5.3.1-2.12.tar.gz

tar xzf confluent-5.3.1-2.12.tar.gz

# /usr/local/bin was empty in the new machine
# needs to be run as root
curl -L https://cnfl.io/cli | sh -s -- -b /usr/local/bin

export PATH=<path-to-confluent>/bin:$PATH

confluent local start



#install java 11
sudo apt install openjdk-11-jre-headless