BASE_DIR=/apps
DATA_API_DIR=${BASE_DIR}/ib_api/data_api

## create base directory
#mkdir ${BASE_DIR}
#cd ${BASE_DIR}
#
## clone app repository
#git clone https://github.com/dali1981/ib_api.git

#create environment for data api
cd ${DATA_API_DIR}
python3 -m venv venv
${DATA_API_DIR}/venv/bin/pip install --upgrade pip setuptools
${DATA_API_DIR}/venv/bin/pip install --upgrade wheel uwsgi

# install dependencies
${DATA_API_DIR}/venv/bin/pip install -r ${DATA_API_DIR}/requirements.txt

# Set Flask environment
export FLASK_CONFIG=production

# Initialize database
${DATA_API_DIR}/venv/bin/python flask_app.py db init
${DATA_API_DIR}/venv/bin/python flask_app.py db migrate

# test app
${DATA_API_DIR}/venv/bin/python flask_app.py runserver

# test the application with uwsgi
#venv/bin/uwsgi -H venv --master --processes 4 --threads 2 --http :5000 --manage -script-name --python-path . --mount /=wsgi:app


# these packege do something that needs to be checked
apt install libpq-dev python3-dev



# these are python packages that run as a command line, check in which environment to install them
pip install --upgrade httpie glances
