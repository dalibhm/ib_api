export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64
sudo apt-get install openjdk-8-jdk

install java before !!!
make sure there is only one java


sudo apt install curl
curl -O http://packages.confluent.io/archive/5.3/confluent-5.3.1-2.12.tar.gz

tar xzf confluent-5.3.1-2.12.tar.gz
tar -xvf confluent-5.3.1-2.12.tar

# /usr/local/bin was empty in the new machine
# needs to be run as root
curl -L https://cnfl.io/cli | sh -s -- -b /usr/local/bin

export PATH=<path-to-confluent>/bin:$PATH
# /usr/local/bin is cormally in the path

sudo add-apt-repository ppa:openjdk-r/ppa
sudo apt-get update


confluent local start



#install java 11
sudo apt install openjdk-11-jre-headless