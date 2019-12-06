curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d '{
  "name": "stock-listing",
  "config": {
        "connector.class": "io.confluent.connect.jdbc.JdbcSourceConnector",
        "connection.url": "jdbc:postgresql://localhost:5432/ib_test",
        "connection.user": "ib_test",
        "connection.password": "ib_test",
        "mode": "bulk",
        "topic.prefix": "postgres-stocks",
        "query": "SELECT con_id, symbol, currency, exchange FROM stocks LIMIT 1;",
        "name": "stock-listing"
      }
    }'
