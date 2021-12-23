

## Usage <a name = "usage"></a>


Local 
```
docker compose up --build
```
Tests
```
docker compose -f docker-compose.yml run tdd-services pytest -vv
```

### Aerich

Initialize the config file and migrations location:
```
docker compose -f docker-compose.yml run tdd-services aerich init -t app.db.TORTOISE_ORM
```


aerich init-db