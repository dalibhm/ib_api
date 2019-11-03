#alias python='winpty python.exe'

BASE_DIR=/c/Users/moham/workspace/ib_api

## create base directory
#mkdir ${BASE_DIR}
#cd ${BASE_DIR}
#
## clone app repository
#git clone https://github.com/dali1981/ib_api.git

#create environment for services
for service in ib_client fundamental_data stock_listing runner
do
  python -m venv ${BASE_DIR}/${service}/venv
  ${BASE_DIR}/${service}/venv/Scripts/pip install --upgrade --user pip setuptools
  ${BASE_DIR}/${service}/venv/Scripts/pip install --user -r ${BASE_DIR}/${service}/requirements.txt
done


git-bash ${BASE_DIR}/fundamental_data python3 server
