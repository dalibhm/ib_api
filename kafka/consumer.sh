confluent local consume historical_data -- --value-format avro --from-beginning
confluent local list connectors

confluent local destroy

bin/kafka-topics --zookeeper localhost:2181 --delete --topic test