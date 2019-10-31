## Docker Commands

### Alle Docker Container starten
```
docker-compose up
```

### Beenden aller Container
```
Ctrl + C
docker rm $(docker ps -aq)
```

oder

```
docker-compose down
```

### Images herunterladen
```
docker pull <image>
```