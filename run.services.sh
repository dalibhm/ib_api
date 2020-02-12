#export environment=production
APP_DIR=/Users/dali/workspace/ibapp
#cd ${APP_DIR}/historical_data/; venv/bin/python historical_data_server.py & disown
cd ${APP_DIR}/fundamental_data/fundamental_data; ../venv/bin/python fundamental_server.py & disown
cd ${APP_DIR}/contracts/contract_service; ../venv/bin/python contract_server.py & disown
cd ${APP_DIR}/stock_listing/stock_listing; ../venv/bin/python stock_listing_server.py & disown
#cd ${APP_DIR}/ib_client/ibclient; ../venv/bin/python app.py & disown

#./runner/venv/bin/python ./runner/runner.py --historical --start-date 1999-01-01 --end-date 2019-11-27 --stock-number 10000 & disown
#cd ${APP_DIR}/runner;./venv/bin/python ./runner.py --historical --start-date 1999-01-01 --end-date 2019-11-27  & disown
#cd ${APP_DIR}/runner;./venv/bin/python ./runner.py --historical --start-date 2019-01-01 --end-date 2019-11-27  & disown

