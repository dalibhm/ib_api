sudo apt-get install python3-venv

BASE_DIR=.

## create base directory
#mkdir ${BASE_DIR}
#cd ${BASE_DIR}
#
## clone app repository
#git clone https://github.com/dali1981/ib_api.git

#create environment for services
for service in ib_client fundamental_data stock_listing runner
do
  python3 -m venv ${BASE_DIR}/${service}/venv
  ${BASE_DIR}/${service}/venv/bin/pip install --upgrade pip setuptools
  ${BASE_DIR}/${service}/venv/bin/pip install -r ${BASE_DIR}/${service}/requirements.txt
done


./historical_data/venv/bin/python ./historical_data/historical_data_server.py & disown
./venv/bin/python ./historical_data_server.py & disown
./ib_client/venv/bin/python ./ib_client/app.py & disown
./venv/bin/python app.py & disown
./runner/venv/bin/python ./runner/runner.py --historical --start-date 1999-01-01 --end-date 2019-11-27 --stock-number 10000 & disown
./venv/bin/python ./runner.py --historical --start-date 1999-01-01 --end-date 2019-11-27 --stock-number 40000 & disown