# Spark Hello-World

## Vorberietung
docker-compose up

In der Console nach :8888 suche und die URL in den Browser kopieren

## Übung
1. Neues Notebook für Python 3 erstellen
2. Name vergebe

Python Kafka Library installieren
```
!pip install kafka-python
```

Imports
```python
from kafka import KafkaConsumer, KafkaProducer
from json import dumps, loads
from time import sleep
```

Producer erstellen
```python
producer = KafkaProducer(bootstrap_servers=["broker:9093"], value_serializer=lambda x: dumps(x).encode('utf-8'))

for i in range(10):
    data = {"name": "BSC Young Boys", "count": i}
    producer.send("academy-topic", value=data)
    sleep(1)
```

Consumer erstellen
```python
consumer = KafkaConsumer("academy-topic", 
                         auto_offset_reset="earliest",
                         bootstrap_servers=["broker:9093"], 
                         value_deserializer = loads,
                         consumer_timeout_ms=1000)

for msg in consumer:
    print(msg.value)
```