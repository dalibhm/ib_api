#!/usr/bin/env bash

cp /apps/ib_api/data_api/server/data_api.nginx /etc/nginx/sites-enabled/data_api.nginx
update-rc.d nginx enable
service nginx restart