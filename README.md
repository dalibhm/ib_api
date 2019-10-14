# ib_api

## data_api

### Contracts
* GET api/contracts
* GET api/contracts/ &lt string:con_id &gt
* POST api/contracts

### Contract details
* GET api/contracts/details
* GET api/contracts/&ltstring:con_id>/details
* POST api/contracts/details

### Exchanges
* GET api/exchanges
* GET api/exchanges/&ltstring:code>
* POST api/exchanges

### Stocks
* GET api/stocks
* GET api/stocks/&ltstring:con_id>
* POST api/stocks

### Historical data
* GET api/historical_data/&ltstock>
* GET api/historical_data/&ltstock>/<whatToShow>/<date>
* POST api/historical_data/

### Fundamental data

* GET api/fundamental_data/calendar_reports
* GET api/fundamental_data/calendar_reports/&ltstock>
* GET api/fundamental_data/calendar_reports/&ltsymbol>/&ltreport_date>

* POST api/fundamental_data/calendar_reports
