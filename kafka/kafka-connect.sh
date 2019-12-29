curl http://localhost:8083/connectors

curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d '{
  "name": "stock-listing",
  "config": {
        "connector.class": "io.confluent.connect.jdbc.JdbcSourceConnector",
        "connection.url": "jdbc:postgresql://localhost:5432/ib_test",
        "connection.user": "ib_test",
        "connection.password": "ib_test",
        "mode": "bulk",
        "topic.prefix": "postgres-",
        "table.whitelist": "stocks",
        "transforms": "ValueToKey",
        "transforms.ValueToKey.fields": "symbol, exchange",
        "transforms.ValueToKey.type": "org.apache.kafka.connect.transforms.ValueToKey",
        "name": "stock-listing"
      }
    }'

curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d '{
  "name": "stock-listing",
  "config": {
        "connector.class": "io.confluent.connect.jdbc.JdbcSourceConnector",
        "connection.url": "jdbc:postgresql://localhost:5432/ib_test",
        "connection.user": "ib_test",
        "connection.password": "ib_test",
        "mode": "bulk",
        "topic.prefix": "postgres-",
        "table.whitelist": "stocks",
        "transforms": "ValueToKey",
        "transforms.ValueToKey.fields": "symbol, exchange",
        "transforms.ValueToKey.type": "org.apache.kafka.connect.transforms.ValueToKey",
        "name": "stock-listing"
      }
    }'

cd ~/Downloads/confluent-5.3.1/
bin/kafka-avro-console-consumer.sh --bootstrap-server localhost:9092\
 --property schema.registry.url=http://localhost:8081\
  --property print.key=true\
   --from-beginning\
    --topic postgres-stocks


bin/kafka-avro-console-consumer.sh --bootstrap-server localhost:9092\
 --property schema.registry.url=http://localhost:8081\
  --property print.key=true\
   --from-beginning\
    --topic historical_data_requests

bin/kafka-topics --zookeeper localhost:2181 --delete --topic historical_data_requests_06


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

# or
confluent load sink-1 -d sink-postgres.json


# logs

confluent local log connect > ~/log_connect.log


bin/confluent-hub install debezium/debezium-connector-mongodb:latest


curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d '{
    "name" : "mongo-sink-1",
    "config":{
      "tasks.max": 1,
      "connector.class": "com.mongodb.kafka.connect.MongoSinkConnector",
      "topics": "historical_data_bis",
      "key.converter": "io.confluent.connect.avro.AvroConverter",
      "value.converter": "io.confluent.connect.avro.AvroConverter",
      "connection.uri": "mongodb://localhost:27017",
      "database": "ib_test",
      "collection": "historical_data"
      }
}'