#!/bin/bash
docker pull cassandra
docker pull mongo
docker pull confluentinc/cp-zookeeper
docker pull confluentinc/cp-enterprise-kafka
docker pull bde2020/spark-master:2.3.0-hadoop2.7
docker pull bde2020/spark-worker:2.3.0-hadoop2.7
docker pull jupyter/all-spark-notebook:latest
docker pull dylanmei/zeppelin
docker pull bde2020/hadoop-namenode:1.1.0-hadoop2.8-java8
docker pull bde2020/hadoop-datanode:1.1.0-hadoop2.8-java8
