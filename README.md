# ib_api

# data_api
GET api/contracts
GET api/contracts/<string:con_id>
POST api/contracts

GET api/contracts/details
GET api/contracts/<string:con_id>/details/
POST api/contracts/details

GET api/exchanges
GET api/exchanges/<string:code>
POST api/exchanges

GET api/stocks
GET api/stocks/<string:con_id>
POST api/stocks

GET api/historical_data/<stock>
GET api/historical_data/<stock>/<whatToShow>/<date>
POST api/historical_data/

# Fundamental data

GET api/fundamental_data/calendar_reports
GET api/fundamental_data/calendar_reports/<stock>
GET api/fundamental_data/calendar_reports/<symbol>/<report_date>

POST api/fundamental_data/calendar_reports
