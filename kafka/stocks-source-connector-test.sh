curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d '{
  "name": "stock-listing",
  "config": {
        "connector.class": "io.confluent.connect.jdbc.JdbcSourceConnector",
        "connection.url": "jdbc:postgresql://localhost:5432/ib_test",
        "connection.user": "ib_test",
        "connection.password": "ib_test",
        "mode": "bulk",
        "topic.prefix": "postgres-stocks",
        "query": "SELECT con_id, symbol, currency, exchange FROM stocks LIMIT 4000;",
        "name": "stock-listing"
      }
    }'

curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d '{
  "name": "stock-10",
  "config": {
        "connector.class": "io.confluent.connect.jdbc.JdbcSourceConnector",
        "connection.url": "jdbc:postgresql://localhost:5432/ib_test",
        "connection.user": "ib_test",
        "connection.password": "ib_test",
        "mode": "bulk",
        "topic.prefix": "postgres-stocks",
        "query": "SELECT con_id, symbol, currency, exchange FROM stocks_10;",
        "poll.interval.ms" : "86400000"
      }
    }'
curl -X DELETE localhost:8083/connectors/stock-10
bin/kafka-topics --zookeeper localhost:2181 --delete --topic s10

curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d '{
  "name": "stock-listing",
  "config": {
        "connector.class": "io.confluent.connect.jdbc.JdbcSourceConnector",
        "connection.url": "jdbc:postgresql://192.168.1.97:5432/ib_test",
        "connection.user": "ib_test",
        "connection.password": "ib_test",
        "mode": "bulk",
        "topic.prefix": "postgres-stocks",
        "query": "SELECT DISTINCT ON (con_id) con_id, symbol, currency, exchange FROM stocks LIMIT 4000;",
        "name": "stock-listing"
      }
    }'