# shellcheck disable=SC2016
curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d '{
    "name": "sink-postgres-1",
    "config": {
        "connector.class": "io.confluent.connect.jdbc.JdbcSinkConnector",
        "value.converter": "io.confluent.connect.avro.AvroConverter",
        "value.converter.schema.registry.url": "http://localhost:8081",
        "connection.url": "jdbc:postgresql://192.168.1.97:5432/ib_test",
        "connection.user": "ib_test",
        "connection.password": "ib_test",
        "topics": "historical-data",
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