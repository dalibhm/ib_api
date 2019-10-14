# ib_api

## 1- data_api
This service is the data API. It allows to write to and read from the data repository.

### Contracts
* GET api/contracts
* GET api/contracts/{string:con_id}
* POST api/contracts

### Contract details
* GET api/contracts/details
* GET api/contracts/{tstring:con_id}/details
* POST api/contracts/details

### Exchanges
* GET api/exchanges
* GET api/exchanges/{string:code}
* POST api/exchanges

### Stocks
* GET api/stocks
* GET api/stocks/{string:con_id}
* POST api/stocks

### Historical data
* GET api/historical_data/{stock}
* GET api/historical_data/{stock}/{whatToShow}/{date}
* POST api/historical_data/

### Fundamental data

* GET api/fundamental_data/calendar_reports
* GET api/fundamental_data/calendar_reports/{stock}
* GET api/fundamental_data/calendar_reports/{symbol>/{treport_date}

* POST api/fundamental_data/calendar_reports

## 2- IB_API

This service receives a GRPC request and connects to IB Gateway using the Python IB Client to get the data from Interactive Brokers, then call the data API in order to write the result to the database.

#### Responsibilty 
* DATA API client
* IB API client
* Request Manager
* Settings : **settings need to be available for all the projects**
* Logging

The service gets set up and listens to incoming requests, forward them to IB API and writes the response in the data store using DATA API.


## 3- Scripts
Contain scripts that launch the data requests.
* fundamental clients
* historical clients
* services : **check what services are used for**

## 4- STOCK LIST
* reads exchanges from Interactive Brokers website and writes them to the datastore. This step does not need to be done frequently.
* reads stocks from Interactive Brokers website and wites them to the datastore.
  * **something has to be done here to detect new stocks and discontinued stocks**

