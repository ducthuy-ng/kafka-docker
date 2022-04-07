from kafka import KafkaConsumer

import json
import pprint


if __name__ == "__main__":
  consumer = KafkaConsumer("test-jdbc-source-testtable",
                           bootstrap_servers="localhost:29091,localhost:29092,localhost:29093")
  
  for msg in consumer:
    pprint.pprint(json.loads(msg.value))