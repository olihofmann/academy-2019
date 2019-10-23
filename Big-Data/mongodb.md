# MongoDB

## Vorbereitung
### Arbeiten mit RoboMongo
docker run --name academy-mongo -p 27017:27017 -d mongo
Robo Mongo unter https://robomongo.org/download herunterladen

### Arbeiten mit dem mongo db cli
docker run -it --link cas-mongo:mongo --rm mongo sh -c 'exec mongo "$MONGO_PORT_27017_TCP_ADDR:$MONGO_PORT_27017_TCP_PORT/test"'

## Übung starten

Für den Anfang gibt es sechs einfache Konzepte, die wir verstehen müssen.
1. MongoDB hat das gleiche Konzept einer Datenbank, mit der Sie wahrscheinlich bereits vertraut sind (oder ein Schema für youOracle Leute). Innerhalb einer MongoDB-Instanz können Sie null oder mehr Datenbanken haben, die jeweils als High-Level-Container für alles andere dienen.
2. Eine Datenbank kann null oder mehr Collection haben. Eine Collection ist in der relationalen Welt eine Table
3. Collections bestehen aus null oder mehr Documents. Auch hier kann man sich ein Documents als eine Row vorstellen. 
4. Ein Document besteht aus einem oder mehreren Feldern, von denen Sie wahrscheinlich annehmen können, dass sie Columns ähneln. 
5. Indizes in MongoDB funktionieren weitgehend wie ihre RDBMS-Pendants. 
6. Die Cursors sind anders als die anderen fünf Konzepte, aber sie sind wichtig genug und werden oft übersehen, dass sie meiner Meinung nach ihrer eigenen Diskussion würdig sind. Das Wichtigste, was man über Cursors verstehen sollte, ist, dass, wenn man MongoDB nach Daten fragt, einen Zeiger auf die Ergebnismenge namens Cursor zurückgibt, mit der wir Dinge wie Zählen oder Überspringen tun können, bevor wir tatsächlich Daten herunterziehen. 

#### Übung 1
```
db.unicorns.insert({name: 'Aurora', gender: 'f', weight: 450})

db.unicorns.find()

db.system.indexes.find()

db.unicorns.insert({name: 'Leto', gender: 'm', home: 'Arrakeen', worm: false})

db.unicorns.remove({})
```

#### Übung 2
```
db.unicorns.insert({name: 'Horny', 
					dob: new Date(1992,2,13,7,47), 
					loves: ['carrot','papaya'], 
					weight: 600,
                    gender: 'm',
					vampires: 63}); 

db.unicorns.insert({name: 'Aurora',
					dob: new Date(1991, 0, 24, 13, 0), 
					loves: ['carrot', 'grape'], 
					weight: 450,
					gender: 'f',
					vampires: 43}); 

db.unicorns.insert({name: 'Unicrom',
					dob: new Date(1973, 1, 9, 22, 10),
					loves: ['energon', 'redbull'], 
					weight: 984,
					gender: 'm',
					vampires: 182}); 

db.unicorns.insert({name: 'Roooooodles',
					dob: new Date(1979, 7, 18, 18, 44), 
					loves: ['apple'],
					weight: 575,
					gender: 'm',
					vampires: 99}); 

db.unicorns.insert({name: 'Solnara',
					dob: new Date(1985, 6, 4, 2, 1), 
					loves:['apple', 'carrot','chocolate'], 
					weight:550,
					gender:'f',
					vampires:80}); 

db.unicorns.insert({name:'Ayna',
					dob: new Date(1998, 2, 7, 8, 30), 
					loves: ['strawberry', 'lemon'], 
					weight: 733,
					gender: 'f',
					vampires: 40}); 

db.unicorns.insert({name:'Kenny',
					dob: new Date(1997, 6, 1, 10, 42), 
					loves: ['grape', 'lemon'],
					weight: 690,
					gender: 'm',
					vampires: 39}); 

db.unicorns.insert({name: 'Raleigh',
					dob: new Date(2005, 4, 3, 0, 57), 
					loves: ['apple', 'sugar'], 
					weight: 421,
					gender: 'm',
					vampires: 2}); 

db.unicorns.insert({name: 'Leia',
					dob: new Date(2001, 9, 8, 14, 53), 
					loves: ['apple', 'watermelon'], 
					weight: 601,
					gender: 'f',
					vampires: 33}); 

db.unicorns.insert({name: 'Pilot',
					dob: new Date(1997, 2, 1, 5, 3), 
					loves: ['apple', 'watermelon'], 
					weight: 650,
					gender: 'm',
					vampires: 54}); 

db.unicorns.insert({name: 'Nimue',
					dob: new Date(1999, 11, 20, 16, 15), 
					loves: ['grape', 'carrot'],
					weight: 540,
					gender: 'f'});

db.unicorns.insert({name: 'Dunx',
					dob: new Date(1976, 6, 18, 18, 18), 
					loves: ['grape', 'watermelon'], 
					weight: 704,
					gender: 'm',
					vampires: 165});
```

#### Übung 3
```
db.unicorns.find({gender: 'm', weight: {$gt: 700}})

//or (not quite the same thing, but for //demonstration purposes) 
db.unicorns.find({gender: {$ne: 'f'}, weight: {$gte: 701}})

db.unicorns.find({ vampires: {$exists: false} })

db.unicorns.find({ loves: {$in : ['apple','orange']} }) 

db.unicorns.find({gender: 'f', $or: [ {loves: 'apple'}, {weight: {$lt: 500}} ] })

db.unicorns.find( {_id: ObjectId("<the-object-id>")})
```

#### Übung 4
```
db.unicorns.update( {name: 'Roooooodles'}, {weight: 590} )

db.unicorns.find({name: 'Roooooodles'})

db.unicorns.update({weight: 590},  {$set: { name: 'Roooooodles',
										dob: new Date(1979, 7, 18, 18, 44), 
										loves: ['apple'],
										gender: 'm', 
										vampires: 99}})

db.unicorns.find({name: 'Roooooodles'})

db.unicorns.update({name: 'Pilot'}, {$inc: {vampires: -2}})
db.unicorns.find({name: 'Pilot'})

db.unicorns.update({name: 'Aurora'}, {$push: {loves: 'sugar'}})
db.unicorns.find({name: 'Aurora'})

db.hits.update({page: 'unicorns'}, {$inc: {hits: 1}});
db.hits.find();

db.hits.update({page: 'unicorns'}, {$inc: {hits: 1}}, {upsert:true});
db.hits.find();

db.hits.update({page: 'unicorns'}, {$inc: {hits: 1}}, {upsert:true});
db.hits.find();

db.unicorns.update({}, {$set: {vaccinated: true }});
db.unicorns.find({vaccinated: true});

db.unicorns.update({}, {$set: {vaccinated: true }}, {multi:true});
db.unicorns.find({vaccinated: true});
```

#### Übung 5
```
db.unicorns.find({}, {name: 1});

//heaviest unicorns first
db.unicorns.find().sort({weight: -1})

//by unicorn name then vampire kills:
db.unicorns.find().sort({name: 1, vampires: -1})

db.unicorns.find().sort({weight: -1}).limit(2).skip(1)

db.unicorns.count({vampires: {$gt: 50}})

db.unicorns.find({vampires: {$gt: 50}}).count()
```

#### Übung 6
```
db.employees.insert({_id: ObjectId( "4d85c7039ab0fd70a117d730"), name: 'Leto'})

db.employees.insert({_id: ObjectId( "4d85c7039ab0fd70a117d731"), name: 'Duncan',
                     manager: ObjectId( "4d85c7039ab0fd70a117d730")});

db.employees.insert({_id: ObjectId( "4d85c7039ab0fd70a117d732"), name: 'Moneo',
                    manager: ObjectId( "4d85c7039ab0fd70a117d730")});

db.employees.find({manager: ObjectId( "4d85c7039ab0fd70a117d730")})

db.employees.insert({_id: ObjectId( "4d85c7039ab0fd70a117d733"), 
                     name: 'Siona',
                     manager: [ObjectId( "4d85c7039ab0fd70a117d730"),
                              ObjectId( "4d85c7039ab0fd70a117d732")]       
                   })

db.employees.find({manager: ObjectId( "4d85c7039ab0fd70a117d730")})

db.employees.insert({_id: ObjectId( "4d85c7039ab0fd70a117d734"), 
                     name: 'Ghanima',
                     family: {mother: 'Chani',
                             father: 'Paul',
                             brother: ObjectId( "4d85c7039ab0fd70a117d730")}
                    })

db.employees.find({ 'family.mother': 'Chani'})

db.employees.insert({_id: ObjectId( "4d85c7039ab0fd70a117d735"), 
					 name : 'Chani', 
					 family : [ {relation:'mother', name: 'Chani'}, 
					           {relation:'father', name: 'Paul'}, 
					           {relation:'brother', name: 'Duncan'}
					         ]})

db.users.insert({name: 'leto',
                email: 'leto@dune.gov',
                addresses: [{street: "229 W. 43rd St",
                             city: "New York", 
                             state:"NY",
                             zip:"10036"}, 
                            {street: "555 University",
                             city: "Palo Alto", 
                             state:"CA",
                             zip:"94107"}]})
```

#### Übung 7
```
db.unicorns.aggregate([{$group:{_id:'$gender', total: {$sum:1}}}])

db.unicorns.aggregate([{$match: {weight:{$lt:600}}}, 
						{$group: {_id:'$gender',
						          total:{$sum:1},
								  avgVamp:{$avg:'$vampires'}}}, 
						{$sort:{avgVamp:-1}} ])

db.unicorns.aggregate([{$unwind:'$loves'}, 
                       {$group: {_id:'$loves', 
                                 total:{$sum:1}, 
                                 unicorns:{$addToSet:'$name'}}}, 
                       {$sort:{total:-1}},
                       {$limit:1} ])
```