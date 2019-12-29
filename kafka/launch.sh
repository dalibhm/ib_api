bin/kafka-topics --zookeeper localhost:2181 --delete --topic historical_data
bin/kafka-topics --zookeeper localhost:2181 --delete --topic historical_data_requests
bin/kafka-topics --zookeeper localhost:2181 --delete --topic historical_data_error
bin/kafka-topics --zookeeper localhost:2181 --delete --topic historical_data_end
bin/kafka-topics --zookeeper localhost:2181 --delete --topic postgres-stocks

cd ~/confluent-5.3.1/; confluent local start


curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d '{
  "name": "stocks-amex",
  "config": {
        "connector.class": "io.confluent.connect.jdbc.JdbcSourceConnector",
        "connection.url": "jdbc:postgresql://192.168.1.97:5432/ib_test",
        "connection.user": "ib_test",
        "connection.password": "ib_test",
        "mode": "bulk",
        "topic.prefix": "postgres-stocks",
        "query": "SELECT con_id, symbol, currency, exchange FROM stocks_amex;",
        "poll.interval.ms" : "86400000"
      }
    }'

curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d '{
    "name": "sink-postgres",
    "config": {
        "connector.class": "io.confluent.connect.jdbc.JdbcSinkConnector",
        "value.converter": "io.confluent.connect.avro.AvroConverter",
        "value.converter.schema.registry.url": "http://localhost:8081",
        "connection.url": "jdbc:postgresql://192.168.1.97:5432/ib_test",
        "connection.user": "ib_test",
        "connection.password": "ib_test",
        "topics": "historical_data",
        "insert.mode": "upsert",
        "auto.create": true,
        "auto.evolve": true,
        "pk.mode": "record_value",
        "pk.fields": "symbol,exchange,currency,date",
        "transforms": "InsertField",
        "transforms.InsertField.timestamp.field": "created_ts",
        "transforms.InsertField.type": "org.apache.kafka.connect.transforms.InsertField$Value"
    }
}'
