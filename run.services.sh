./historical_data/venv/bin/python ./historical_data/historical_data_server.py & disown
./venv/bin/python ./historical_data_server.py & disown
./ib_client/venv/bin/python ./ib_client/app.py & disown
./venv/bin/python app.py & disown
#./runner/venv/bin/python ./runner/runner.py --historical --start-date 1999-01-01 --end-date 2019-11-27 --stock-number 10000 & disown
#./venv/bin/python ./runner.py --historical --start-date 1999-01-01 --end-date 2019-11-27 --stock-number 40000 & disown

