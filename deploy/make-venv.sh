BASE_DIR=..

## create base directory
#mkdir ${BASE_DIR}
#cd ${BASE_DIR}
#
## clone app repository
#git clone https://github.com/dali1981/ib_api.git

#create environment for services
apt install python3-venv python3-pip

for service in runner ib_client stock_listing contracts historical_data fundamental_data
do
  python3 -m venv ${BASE_DIR}/${service}/venv
  ${BASE_DIR}/${service}/venv/bin/pip install --upgrade pip setuptools
  ${BASE_DIR}/${service}/venv/bin/pip install -r ${BASE_DIR}/${service}/requirements.txt
done
cd ${BASE_DIR}/resources
../ib_client/venv/bin/python3 setup.py install

venv/bin/pip3 install -i https://testpypi.python.org/pypi psycopg2==2.7.7