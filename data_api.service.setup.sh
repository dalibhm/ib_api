#!/usr/bin/env bash

cp /apps/ib_api/data_api/server/data_api.service /etc/systemd/system/data_api.service

systemctl daemon-reload
systemctl start data_api
systemctl status data_api
systemctl enable data_api