
#pip3 install virtualenv
#cd /apps
python3 -m venv venv
source venv/bin/activate
sudo venv/bin/pip install --upgrade pip setuptools
sudo venv/bin/pip install --upgrade wheel
sudo venv/bin/pip install --upgrade uwsgi

# the line below launches something
venv/bin/uwsgi -H venv --master --processes 4 --threads 2 --http :5000 --manage -script-name --python-path . --mount /=wsgi:app


apt install libpq-dev python3-dev

venv/bin/pip install -r requirements.txt


pip3 install --upgrade pip setuptools
pip install --upgrade httpie glances
