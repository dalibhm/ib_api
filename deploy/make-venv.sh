BASE_DIR=..

## create base directory
#mkdir ${BASE_DIR}
#cd ${BASE_DIR}
#
## clone app repository
#git clone https://github.com/dali1981/ib_api.git

#create environment for services
apt ger python3-venv python3-pip

for service in runner ib_client stock_listing contracts historical_data fundamental_data
do
  python3 -m venv ${BASE_DIR}/${service}/venv
  ${BASE_DIR}/${service}/venv/bin/pip install --upgrade pip setuptools
  ${BASE_DIR}/${service}/venv/bin/pip install -r ${BASE_DIR}/${service}/requirements.txt
done

${BASE_DIR}/ib_client/venv/bin/python3 ${BASE_DIR}/resources/setup.py install