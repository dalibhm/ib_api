#! /bin/bash

brew services start postgresql
brew services start rabbitmq

open -a /Users/dali/Applications/IB\ Gateway\ 972/IB\ Gateway\ 972.app/

source activate IB &
/anaconda3/envs/IB/bin/python /Users/dali/workspace/rabbitmq/historical_data_writer.py &
/anaconda3/envs/IB/bin/python /Users/dali/workspace/IB/Python/Testbed/program_.py &
