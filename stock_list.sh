#!/usr/bin/env bash

cd /apps/ib_api/ib_python/stock_list

python3 -m venv s_venv
sudo s_venv/bin/pip install --upgrade pip setuptools
sudo s_venv/bin/pip install -r requirements.txt

s_venv/bin/python3 program.py