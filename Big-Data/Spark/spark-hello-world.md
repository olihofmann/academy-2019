# Spark Hello-World

## Vorberietung
docker-compose up -d

## Dokumentation Spark
https://spark.apache.org/docs/latest/api/python/index.html

## Übung 1

#### Upload der Daten in HDFS
Upload der Daten in HDFS mittels CLI
```
docker exec -it namenode bash

hdfs dfs -mkdir -p input

cd data/
hdfs dfs -copyFromLocal big.txt input

hdfs dfs -ls input
```

## Übung 2

#### Word Count umsetzen
1. Navigieren Sie in einem Browserfenster zu http://docker-host-ip:38080, es sollte der Apache Zeppelin Startbildschirm angezeigt werden.
2. Um ein neues Zeppelin-Notebook zu erstellen, klicken Sie auf den Link "Create new note"
3. Note Name setzen und spark als Interpreter auswählen

Daten aus HDFS laden
```python
%pyspark
lines = sc.textFile("hdfs://namenode:8020/user/root/input/big.txt")
```

Text in Wörter splitten
```python
%pyspark
words = lines.flatMap(lambda line: line.split(" "))
```

Count by Word
```python
%pyspark
counts = words.map(lambda word: (word,1)).reduceByKey(lambda a, b : a + b)
```

Count RDD in HDFS speichern
```python
%pyspark
counts.saveAsTextFile("hdfs://namenode:8020/user/root/output")
```

```
Output anschauen
hdfs dfs -cat output/part-00000 | more
```
