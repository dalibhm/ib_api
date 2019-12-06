confluent local consume postgres-stocks -- --value-format avro --from-beginning

confluent local destroy

bin/kafka-topics --zookeeper localhost:2181 --delete --topic test