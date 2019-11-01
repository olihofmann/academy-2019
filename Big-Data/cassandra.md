# Cassandra

## Vorberietung

docker run -p 9042:9042 --name academy-cassandra -d cassandra

docker run-it --link academy-cassandra:cassandra --rm cassandra sh -c 'exec cqlsh "$CASSANDRA_PORT_9042_TCP_ADDR"'

## Cassandra Dokumentation
http://cassandra.apache.org/doc/latest/cql/

## Übung 1

#### Keyspace erstellen
Keyspace in Cassandra ist das Äquivalent zu Datenbank/Schema in relationalen Datenbanken.

```
CREATE KEYSPACE training WITH replication ={'class':'SimpleStrategy','replication_factor':1};

USE training;

DESCRIBE KEYSPACE training;

SELECT * FROM system_schema.keyspaces;
```

Wir werden SimpleStrategy verwenden, um die Dinge einfach zu halten, denn unser Cassandra-Setup ist nur ein einzelner Knoten. In der Produktionsumgebung, wo es üblich ist, mehrere Rechenzentren zu haben, wird NetworkTopologyStrategy im Allgemeinen verwendet, weil es die Daten besser auf die Rechenzentren verteilt.

#### User Table erstellen
```
CREATE TABLE user (user_id varchar, age int, email varchar, city varchar, PRIMARY KEY (user_id));

DESCRIBE TABLE user;
```

#### Daten erstellen
```
INSERT INTO user (user_id, age, email, city)VALUES ('psample',32,'peter.sample@somecompany.com','Somecity');

INSERT INTO user (user_id, city) VALUES ('bmuster','OnlyCityKnown');

INSERT INTO user (user_id, age, email) VALUES('bmaier',37,'bob.mayer@example.com');

SELECT * FROM user;
SELECT * FROM user WHERE user_id='psample';
```

#### Daten updaten
```
UPDATE user SET email = 'bmaier@somecorp.com'WHERE user_id = 'bmaier';
SELECT * FROM user WHERE user_id='bmaier';
```

#### Daten löschen
```
DELETE email FROM userWHERE user_id = 'psample';

DELETE FROM userWHERE user_id = 'bmaier';

SELECT * FROM user;
```

#### Truncate
```
TRUNCATE user;
SELECT * FROM user;
```

#### TTL
Eine weitere Möglichkeit, Daten in Cassandra zu löschen, besteht darin, beim Einfügen von Daten eine Ablaufzeit namens TTL (time to live) anzugeben. Dies geschieht mit dem Schlüsselwort USING TTL <secs>. 
```
INSERT INTO user (user_id, age, email) VALUES ('ptest', 99, 'ptest@test.ch') USING TTL 30;
```

## Übung 2
Wir möchten eine Datenbank erstellen, die in der Lage ist, eine Liste der beliebtesten Produkte pro Benutzer zu speichern.
```
CREATE TABLE product (product_id UUID, name text, category text, PRIMARY KEY (product_id));

INSERT INTO product (product_id, name, category) VALUES (dda74010-ea91-11e3-ac10-0800200c9a66,'IPad', 'ELE');

INSERT INTO product (product_id, name, category) VALUES (dda74011-ea91-11e3-ac10-0800200c9a66,'IPod5G', 'ELE')

INSERT INTO product (product_id, name, category) VALUES (dda74012-ea91-11e3-ac10-0800200c9a66,'Harry Potter','BOOK');

INSERT INTO product (product_id, name, category) VALUES (51851d90-ea92-11e3-ac10-0800200c9a66,'Rioja 2007', 'FOOD');

CREATE TABLE favorite (user_id text,product_id UUID,comment text, added_at TIMEUUID, removed_at TIMEUUID, PRIMARY KEY (user_id, product_id));

INSERT INTO favorite(user_id, product_id, comment, added_at) VALUES ('psample', dda74010-ea91-11e3-ac10-0800200c9a66,'need new one soon',now());

INSERT INTO favorite(user_id, product_id, comment, added_at) VALUES ('psample', 51851d90-ea92-11e3-ac10-0800200c9a66,'good rating',now());

SELECT * FROM favorite WHERE user_id = 'psample';

UPDATE favorite SET removed_at = now() WHERE user_id = 'psample'AND product_id = dda74010-ea91-11e3-ac10-0800200c9a66;

CREATE TABLE product_rating (product_id UUID, day TIMESTAMP, one_star COUNTER, two_star COUNTER, three_star COUNTER, PRIMARY KEY(product_id, day)) WITH CLUSTERING ORDER BY (day DESC);

UPDATE product_rating SET one_star = one_star + 1 WHERE product_id = dda74010-ea91-11e3-ac10-0800200c9a66AND day = '2019-05-30';

UPDATE product_rating SET two_star = two_star + 1 WHERE product_id = dda74010-ea91-11e3-ac10-0800200c9a66AND day = '2019-05-30';

UPDATE product_rating SET three_star = three_star + 1 WHERE product_id = dda74010-ea91-11e3-ac10-0800200c9a66AND day = '2019-05-30';

UPDATE product_rating SET one_star = one_star + 1 WHERE product_id = dda74010-ea91-11e3-ac10-0800200c9a66AND day = '2019-05-30';

UPDATE product_rating SET one_star = one_star+ 1 WHERE product_id = dda74010-ea91-11e3-ac10-0800200c9a66AND day = '2019-05-30';

UPDATE product_rating SET one_star = one_star + 1 WHERE product_id = dda74010-ea91-11e3-ac10-0800200c9a66AND day = '2019-05-30';

UPDATE product_rating SET two_star = two_star + 1 WHERE product_id = dda74010-ea91-11e3-ac10-0800200c9a66AND day = '2019-05-31';

UPDATE product_rating SET one_star = one_star + 1 WHERE product_id = dda74010-ea91-11e3-ac10-0800200c9a66AND day = '2019-05-31';

UPDATE product_rating SET one_star = one_star + 1 WHERE product_id = dda74010-ea91-11e3-ac10-0800200c9a66AND day = '2019-05-31';

UPDATE product_rating SET one_star = one_star + 1 WHERE product_id = dda74010-ea91-11e3-ac10-0800200c9a66AND day = '2019-05-31';

UPDATE product_rating SET one_star = one_star + 1 WHERE product_id = dda74010-ea91-11e3-ac10-0800200c9a66AND day = '2019-06-01';

UPDATE product_rating SET two_star = two_star + 1 WHERE product_id = dda74010-ea91-11e3-ac10-0800200c9a66AND day = '2019-06-01';

UPDATE product_rating SET three_star = three_star + 1 WHERE product_id = dda74010-ea91-11e3-ac10-0800200c9a66AND day = '2019-06-02';

UPDATE product_rating SET two_star = two_star + 1 WHERE product_id = dda74010-ea91-11e3-ac10-0800200c9a66AND day = '2019-06-02';

UPDATE product_rating SET two_star = two_star + 1 WHERE product_id = dda74010-ea91-11e3-ac10-0800200c9a66AND day = '2019-06-02';

UPDATE product_rating SET one_star = one_star + 1 WHERE product_id = dda74010-ea91-11e3-ac10-0800200c9a66AND day = '2019-06-02';

SELECT * FROM product_rating WHERE product_id = dda74010-ea91-11e3-ac10-0800200c9a66;

SELECT * FROM product_rating WHERE product_id = dda74010-ea91-11e3-ac10-0800200c9a66AND day >= '2014-06-01';
```







