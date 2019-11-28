curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d '{
  "name": "stock-listing",
  "config": {
        "connector.class": "io.confluent.connect.jdbc.JdbcSourceConnector",
        "connection.url": "jdbc:postgresql://192.168.1.97:5432/ib_test",
        "connection.user": "ib_test",
        "connection.password": "ib_test",
        "mode": "bulk",
        "topic.prefix": "postgres-",
        "table.whitelist": "stocks_unique",
        "transforms": "ValueToKey",
        "transforms.ValueToKey.fields": "symbol, exchange",
        "transforms.ValueToKey.type": "org.apache.kafka.connect.transforms.ValueToKey",
        "name": "stock-listing"
      }
    }'