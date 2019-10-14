# ib_api

## data_api

### Contracts
* GET api/contracts
* GET api/contracts/<string:con_id>
* POST api/contracts

### Contract details
* GET api/contracts/details
* GET api/contracts/<string:con_id>/details/
* POST api/contracts/details

### Exchanges
* GET api/exchanges
* GET api/exchanges/<string:code>
* POST api/exchanges

### Stocks
* GET api/stocks
* GET api/stocks/<string:con_id>
* POST api/stocks

### Historical data
* GET api/historical_data/<stock>
* GET api/historical_data/<stock>/<whatToShow>/<date>
* POST api/historical_data/

### Fundamental data

* GET api/fundamental_data/calendar_reports
* GET api/fundamental_data/calendar_reports/<stock>
* GET api/fundamental_data/calendar_reports/<symbol>/<report_date>

* POST api/fundamental_data/calendar_reports
